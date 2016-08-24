# -*- coding: utf-8 -*-
###
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.db.models import Max
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import transaction
import datetime, time
from django.core.paginator import Paginator

from datetime import timedelta
import sys, traceback

from .models import Item, Order, Ordered_item, Store, Grade, Unit
import json


# 한글테스트
def index(request):
	order_info = []
	global_value = {}

	try:
		# order_info = Order.objects.get(pk=order_id)
		# order_info = Order.objects.order_by('-order_date')[:20]
		order_info = Order.objects.order_by('-order_date')
		global_value['store_list'] = Store.objects.order_by("store_code")
		global_value['item_list'] = Item.objects.order_by("item_code")
		global_value['unit_list'] = Unit.objects.order_by("unit_code")
		global_value['grade_list'] = Grade.objects.order_by("grade_code")

	except Order.DoesNotExist:
		raise Http404("Order does not exist")

	return render(request, 'testapp/home.html', {'order_info': order_info, 'global_value': global_value})


####################################################################
def home(request):
	order_info = []
	global_value = {}
	try:
		# order_info = Order.objects.get(pk=order_id)
		# order_info = Order.objects.order_by('-order_date')[:20]
		# https://docs.djangoproject.com/ja/1.9/topics/db/queries/
		# where clause 에 대해 잘 설명 해둠
		# django 에 pagenation 기능이 있음 , 참고 하자
		# order_info=Order.objects.all().filter(order_store__store_name__contains='서울')
		order_info = Order.objects.all()
		if request.GET.get('search_store', False):
			order_info = order_info.filter(order_store__store_name__contains=request.GET['search_store'])

		if request.GET.get('datepicker_start', False):
			order_info = order_info.filter(order_date__range=(request.GET['datepicker_start'], datetime.date.today()))

		if request.GET.get('datepicker_end', False):
			# end_date =request.GET['datepicker_end'] +  timedelta(days=1)
			date_object = datetime.datetime.strptime(request.GET['datepicker_end'], '%Y-%m-%d')
			end_date = date_object + datetime.timedelta(days=1)
			order_info = order_info.filter(order_date__range=('1920-01-01', end_date))

		global_value['store_list'] = Store.objects.order_by("store_code")
		global_value['item_list'] = Item.objects.order_by("item_code")
		global_value['unit_list'] = Unit.objects.order_by("unit_code")
		global_value['grade_list'] = Grade.objects.order_by("grade_code")
		global_value['page'] = 1

		paginator = Paginator(order_info, 20)
		page_result = paginator.page(1)
	# print order_info[0]
	except Order.DoesNotExist:
		raise Http404("Order does not exist")

	return render(request, 'testapp/home.html', {'order_info': page_result, 'global_value': global_value})


def submit_page(request):
	order_info = []
	global_value = {}
	from_data = json.loads(request.body)
	order_info = Order.objects.all()
	if from_data.get('search_store', False):
		order_info = order_info.filter(order_store__store_name__contains=from_data['search_store'])

	if from_data.get('datepicker_start', False):
		order_info = order_info.filter(order_date__range=(from_data['datepicker_start'], datetime.date.today()))

	if from_data.get('datepicker_end', False):
		date_object = datetime.datetime.strptime(from_data['datepicker_end'], '%Y-%m-%d')
		end_date = date_object + datetime.timedelta(days=1)
		order_info = order_info.filter(order_date__range=('1920-01-01', end_date))


	response_data['page'] = from_data['page'] +1
	paginator = Paginator(order_info, 20)
	order_info = paginator.page(response_data['page'])
	response_data['order_info'] = order_info

	if paginator.count > response_data['page'] :
		response_data['next_page'] = true
	else :
		response_data['next_page'] = false

	response_data['max_page'] =paginator.count

	return HttpResponse(
		json.dumps(response_data),
		content_type="application/json"
	)


# order page
def order(request):
	order_info = []
	global_value = {}
	try:
		# order_info = Order.objects.get(pk=order_id)
		# order_info = Order.objects.order_by('-order_date')[:20]
		order_info = Order.objects.order_by('-order_date')

		global_value['store_list'] = Store.objects.order_by("store_code")
		global_value['item_list'] = Item.objects.order_by("item_code")
		global_value['unit_list'] = Unit.objects.order_by("unit_code")
		global_value['grade_list'] = Grade.objects.order_by("grade_code")

	except Order.DoesNotExist:
		raise Http404("Order does not exist")

	return render(request, 'testapp/order.html', {'order_info': order_info, 'global_value': global_value})


# order control page
def submit_order(request):
	response_data = {}
	response_data['result'] = 'failed'
	order_info_save_ok = False
	order_data = json.loads(request.body)
	if request.method == 'POST':
		if order_data['order_pk']:

			result_query_order = update_order(order_data)
		else:
			result_query_order = insert_order(order_data)

		if order_data.get('ordered_item_list', False) and result_query_order['message'] == "success":

			result_query_order_item = ordered_item_add(order_data['ordered_item_list'], result_query_order['data'])
			response_data['result'] = result_query_order_item['message']
		elif result_query_order['message'] != "success":
			response_data['result'] = result_query_order['message']
		else:
			response_data['result'] = 'No Item list'

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		response_data['result'] = 'method error(POST)'
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)


# 0818--JH
def ordered_item_add(ordered_item_list, order_info):
	result = {}
	try:
		with transaction.atomic():
			sid = transaction.savepoint()
			Ordered_item.objects.filter(ordered_item_order=order_info.order_id).delete()
			for items in ordered_item_list:
				order_item = Ordered_item(
					ordered_item_order=order_info,
					ordered_item_item=Item.objects.get(item_code=items['ordered_item_item_code']),
					ordered_item_unit=Unit.objects.get(unit_code=items['ordered_item_unit_code']),
					ordered_item_unit_price=items['ordered_item_unit_price'].replace(',', ''),
					ordered_item_qty=items['ordered_item_qty'],
					ordered_item_grade=Grade.objects.get(grade_code=items['ordered_item_grade_code']),
					ordered_item_description="items['ordered_item_description']")
				order_item.save()

		transaction.savepoint_commit(sid)
		# print "good"
		# end transaction
		result['message'] = 'success'
	except Exception as e:
		transaction.savepoint_rollback(sid)
		result['message'] = 'canceled #' + e.message
		# traceback.print_exc()  , exception error
		print "[ERROR]ordered_item_add failed # " + e.message

	return result


@transaction.atomic
def update_order(order_data):
	result = {}
	temperr = ""
	try:
		# print "#####\n"+order_data['order_store']
		order_store = Store.objects.get(store_code=order_data['order_store_code'])
		order_info = Order.objects.get(pk=order_data['order_pk'])
		order_info.order_date = timezone.now()
		order_info.order_total_amount = order_data['order_total_amount'].replace(',', '')
		order_info.order_paid_amount = order_data['order_paid_amount'].replace(',', '')
		order_info.order_discounted_amount = order_data['order_discounted_amount'].replace(',', '')
		order_info.order_outstanding_amount = order_data['order_outstanding_amount'].replace(',', '')
		order_info.order_notes = order_data['order_notes']

		order_info.order_store = order_store

		order_info.save()
		result['message'] = 'success'
		result['data'] = order_info

	except Order.DoesNotExist:
		result['message'] = 'Order DoesNotExist'
	except Store.DoesNotExist:
		result['message'] = 'Store DoesNotExist'
	except Exception as e:
		result['message'] = 'message:1' + e.message
	return result


@transaction.atomic
def insert_order(order_data):
	result = {}
	try:
		order_store = Store.objects.get(store_code=order_data['order_store_code'])

		order_info = Order(
			order_date=timezone.now(),
			order_total_amount=order_data['order_total_amount'],
			order_paid_amount=order_data['order_paid_amount'],
			order_discounted_amount=order_data['order_discounted_amount'].replace(',', ''),
			order_outstanding_amount=order_data['order_outstanding_amount'].replace(',', ''),
			order_notes=order_data['order_notes'])
		order_info.order_store = order_store
		order_info.save()
		result['message'] = 'success'
		result['data'] = order_info
	except Store.DoesNotExist:
		result['message'] = 'Store DoesNotExist'
	except Exception as e:
		result['message'] = 'SomeError_insert'
		print e

	return result

################################################################################
