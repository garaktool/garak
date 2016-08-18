#-*- coding: utf-8 -*-

from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.db.models import Max
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import transaction
import sys, traceback
from .models import Item, Order, Ordered_item, Store, Grade, Unit
import json

#한글테스트
def index(request):
	order_info=[]
	global_value={}
	try:
		#order_info = Order.objects.get(pk=order_id)
		#order_info = Order.objects.order_by('-order_date')[:20]
		order_info = Order.objects.order_by('-order_date')
		global_value['store_list'] = Store.objects.order_by("store_code")
		global_value['item_list'] =  Item.objects.order_by("item_code")
		global_value['unit_list'] =  Unit.objects.order_by("unit_code")
		global_value['grade_list'] =  Grade.objects.order_by("grade_code")

	except Order.DoesNotExist:
		raise Http404("Order does not exist")

	return render(request, 'testapp/home.html', {'order_info': order_info,'global_value':global_value})

##edit0810 2
####################################################################
def home(request):
	order_info=[]
	global_value={}
	try:
		#order_info = Order.objects.get(pk=order_id)
		#order_info = Order.objects.order_by('-order_date')[:20]
		order_info = Order.objects.order_by('-order_date')
		global_value['store_list'] = Store.objects.order_by("store_code")
		global_value['item_list'] =  Item.objects.order_by("item_code")
		global_value['unit_list'] =  Unit.objects.order_by("unit_code")
		global_value['grade_list'] =  Grade.objects.order_by("grade_code")

	except Order.DoesNotExist:
		raise Http404("Order does not exist")

	return render(request, 'testapp/home.html', {'order_info': order_info,'global_value':global_value})

#order page
def order(request):
	order_info=[]
	global_value={}
	try:
		#order_info = Order.objects.get(pk=order_id)
		#order_info = Order.objects.order_by('-order_date')[:20]
		order_info = Order.objects.order_by('-order_date')
		global_value['store_list'] = Store.objects.order_by("store_code")
		global_value['item_list'] =  Item.objects.order_by("item_code")
		global_value['unit_list'] =  Unit.objects.order_by("unit_code")
		global_value['grade_list'] =  Grade.objects.order_by("grade_code")

	except Order.DoesNotExist:
		raise Http404("Order does not exist")

	return render(request, 'testapp/order.html', {'order_info': order_info,'global_value':global_value})

#order control page
def submit_order(request):
	response_data={}
	response_data['result'] = 'failed'
	order_info_save_ok = False
	order_data = json.loads(request.body)
	if request.method == 'POST':
		if order_data['order_pk']:

			result_query_order=update_order(order_data)
		else:
			result_query_order=insert_order(order_data)


		if order_data.get('ordered_item_list', False) and result_query_order['message']=="success":

			result_query_order_item=ordered_item_add(order_data['ordered_item_list'],result_query_order['data'])
			response_data['result'] =result_query_order_item['message']
		elif result_query_order['message']!="success":
			response_data['result']=result_query_order['message']
		else:
			response_data['result'] =  'No Item list'

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

#0818--JH
def ordered_item_add(ordered_item_list,order_info):

    print "@@@@@@@@@@@@\n"
    print ordered_item_list
    print "@@@@@@@@@@@@\n"
    print order_info

    result['message'] = 'success'
    return result


@transaction.atomic
def update_order(order_data):
	result={}
	temperr=""
	try:
		#print "#####\n"+order_data['order_store']
		order_store = Store.objects.get(store_code=order_data['order_store_code'])
		order_info = Order.objects.get(pk=order_data['order_pk'])
		order_info.order_date=timezone.now()
		order_info.order_total_amount=order_data['order_total_amount'].replace(',','')
		order_info.order_paid_amount=order_data['order_paid_amount'].replace(',','')
		order_info.order_discounted_amount=order_data['order_discounted_amount'].replace(',','')
		order_info.order_outstanding_amount=order_data['order_outstanding_amount'].replace(',','')
		order_info.order_notes=order_data['order_notes']

		order_info.order_store=order_store

		order_info.save()
		result['message'] = 'success'
		result['data']=order_info

	except Order.DoesNotExist:
		result['message'] = 'Order DoesNotExist'
	except Store.DoesNotExist:
		result['message'] = 'Store DoesNotExist'
	except Exception as e:
		result['message'] = 'message:1'+ e.message
	return result

@transaction.atomic
def insert_order(order_data):
	result={}
	try:
		order_store = Store.objects.get(store_code=order_data['order_store_code'])

		order_info = Order(
			order_date=timezone.now(),
			order_total_amount=order_data['order_total_amount'],
			order_paid_amount=order_data['order_paid_amount'],
			order_discounted_amount=order_data['order_discounted_amount'].replace(',',''),
			order_outstanding_amount=order_data['order_outstanding_amount'].replace(',',''),
			order_notes=order_data['order_notes'])
		order_info.order_store=order_store
		order_info.save()
		result['message'] = 'success'
		result['data']=order_info
	except Store.DoesNotExist:
		result['message'] = 'Store DoesNotExist'
	except Exception as e:
		result['message'] = 'SomeError_insert'
		print e

	return result


################################################################################
