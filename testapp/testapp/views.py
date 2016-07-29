#-*- coding: utf-8 -*-

from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import transaction
import sys, traceback
from .models import Item, Order, Ordered_item, Store, Grade, Unit
import json


def index(request):
    latest_product_list = Item.objects.order_by('-pub_date')[:5]
    context = {'latest_product_list': latest_product_list} 
    return render(request, 'testapp/index.html', context)

####################################################################
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


def submit_order(request):
	response_data={}
	response_data['result'] = 'failed'
	order_info_save_ok = False
	order_data = json.loads(request.body)
	if request.method == 'POST':
		if order_data['order_pk']:#���� order �� ���
			result_query_order=update_order(order_data)
		else:#�ű� order
			result_query_order=insert_order(order_data)
			

		if order_data.get('ordered_item_list', False) and result_query_order['message']=="success":#order itme�� �ְ� , order ���ڵ尡 db�� �� ��� ���� ���
			#order item�� �ٽ� ��� �Ѵ�. , item_list �� order_info ��ü�� �ѱ��.
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


def ordered_item_add(ordered_item_list,order_info):
	result={}
	try:
		with transaction.atomic():
			sid = transaction.savepoint()
			#order �� ���� order item�� ��� �����Ѵ�.
			Ordered_item.objects.filter(ordered_item_order=order_info.order_id).delete()
			for items in ordered_item_list:
				order_item=Ordered_item(
					ordered_item_order=order_info,
					ordered_item_item= Item.objects.get(item_id=items['ordered_item_item']),
					ordered_item_unit=Unit.objects.get(unit_id=items['ordered_item_unit']),
					ordered_item_unit_price = items['ordered_item_unit_price'],
					ordered_item_qty =  items['ordered_item_qty'],
					ordered_item_grade =Grade.objects.get(grade_id=items['ordered_item_grade']),
					ordered_item_description = items['ordered_item_description'])
				order_item.save()
		
		transaction.savepoint_commit(sid)
		#print "good"
        # end transaction
		result['message'] = 'success'
	except Exception as e:
		# Ʈ����� ������ ���� �߻��� �ѹ�ó��
		transaction.savepoint_rollback(sid)
		result['message'] = 'canceled'
		#traceback.print_exc()  , exception error  �󼼳��� ���
		print "[ERROR]ordered_item_add failed" 

	return result





#Ư�� order�� ���� order item ��� ����
#������
def ordered_item_delete(order_pk):
	Ordered_item.objects.filter(order_item=order_pk).delete()
	#delete ����
	#instance = SomeModel.objects.get(id=id)
	#instance.delete()

@transaction.atomic
def update_order(order_data):
	result={}
	temperr=""
	try:
		order_store = Store.objects.get(store_id=order_data['order_store'])
		order_info = Order.objects.get(pk=order_data['order_pk'])
		order_info.order_date=timezone.now() 
		order_info.order_total_amount=order_data['order_total_amount']
		order_info.order_paid_amount=order_data['order_paid_amount']
		order_info.order_discounted_amount=order_data['order_discounted_amount']
		order_info.order_outstanding_amount=order_data['order_outstanding_amount']
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
		result['message'] = e.message
	return result

@transaction.atomic
def insert_order(order_data):
	result={}
	try:
		order_store = Store.objects.get(store_id=order_data['order_store'])

		order_info = Order(
			order_date=timezone.now(), 
			order_total_amount=order_data['order_total_amount'],
			order_paid_amount=order_data['order_paid_amount'],
			order_discounted_amount=order_data['order_discounted_amount'],
			order_outstanding_amount=order_data['order_outstanding_amount'],
			order_notes=order_data['order_notes'])
		order_info.order_store=order_store
		order_info.save()
		result['message'] = 'success'
		result['data']=order_info
	except Store.DoesNotExist:
		result['message'] = 'Store DoesNotExist'
	except Exception as e:# error �߻��� 
		result['message'] = 'SomeError_insert'
		print e
	
	return result

################################################################################
