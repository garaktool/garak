#-*- coding: utf-8 -*-

from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import transaction
from .models import Product, Order, Order_item, Company
import json


class ProductDetailView(generic.DetailView):
	model = Product
	template_name = 'testapp/product_detail.html'

class ProductListView(generic.ListView):
	model = Product
	template_name = 'testapp/product_list.html'
	context_object_name = 'latest_product_list'
	def get_queryset(self):
		return Product.objects.order_by('-pub_date')[:5]

def index(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:5]
    context = {'latest_product_list': latest_product_list} 
    return render(request, 'testapp/index.html', context)

####################################################################
#order page
def order(request):
	order_info=""
	try:
		#order_info = Order.objects.get(pk=order_id)
		order_info = Order.objects.order_by('-order_date')[:10]
		
	except Order.DoesNotExist:
		raise Http404("Order does not exist")

	return render(request, 'testapp/order.html', {'order_info': order_info})

def submit_order_back(request):
	data_post=request.POST
	#dump_data=json.load(data_post['order_item_list'])

	python_data = json.loads(request.body)
	print(python_data['order_item_list'][0])
	print('#############3\n')

	response_data={}
	response_data['result'] = 'Order good'
	return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)

def submit_order(request):
	response_data={}
	response_data['result'] = 'failed'
	order_info_save_ok = False
	order_data = json.loads(request.body)
	if request.method == 'POST':
		if order_data['order_pk']:#기존 order 일 경우
			result_query_order=update_order(order_data)
		else:#신규 order
			result_query_order=insert_order(order_data)
			

		if order_data.get('order_item_list', False) and result_query_order['message']=="success":#order itme이 있고 , order 레코드가 db에 잘 들어 갔을 경우
			#order 에 엮인 order item을 모두 삭제한다.
			#order_item_delete(order_data['order_pk'])
			
			#order item을 다시 등록 한다. , order_item_list 와 order_info 객체를 넘긴다.
			
			result_query_order_item=order_item_add(order_data['order_item_list'],result_query_order['data'])

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

#order item 새로 등록 , savepoint를 활용하여 에러 없이 data 입력 가능, error발생시 자동 rollback됨
@transaction.atomic
def order_item_add(order_item_list,order_info):
	result={}
	sid = transaction.savepoint()
	#order 에 엮인 order item을 모두 삭제한다.
	Order_item.objects.filter(order=order_info.id).delete()
	try:
		for items in order_item_list:
			order_item=Order_item(
				order=order_info,
				unit_price = items['unit_price'],
				amount =  items['amount'],
				grade =items['grade'],
				description = items['description'])

			product_info=Product.objects.get(id=items['product'])
			order_item.product=product_info
			order_item.save()
		transaction.savepoint_commit(sid)
        # end transaction
		result['message'] = 'success'
		return result
	except Exception:
		# 트랜잭션 내에서 에러 발생시 롤백처리
		transaction.savepoint_rollback(sid)
		result['message'] = 'canceled'
		return result
	

#특정 order에 엮인 order item 모두 삭제
def order_item_delete(order_pk):
	Order_item.objects.filter(order=order_pk).delete()
	#delete 예제
	#instance = SomeModel.objects.get(id=id)
	#instance.delete()

def update_order(order_data):
	result={}
	try:
		selling_partner = Company.objects.get(id=order_data['selling_partner'])
		order_info = Order.objects.get(pk=order_data['order_pk'])
		order_info.order_date=timezone.now() 
		order_info.order_amount=order_data['order_amount']
		order_info.collect_money=order_data['collect_money']
		order_info.subtract_amount=order_data['subtract_amount']
		order_info.outstanding_amount=order_data['outstanding_amount']
		order_info.description=order_data['description']
		order_info.selling_partner=selling_partner
		order_info.save()
		result['message'] = 'success'
		result['data']=order_info
	except Order.DoesNotExist:
		result['message'] = 'Order DoesNotExist'
	except Company.DoesNotExist:
		result['message'] = 'Company DoesNotExist'
	except :
		result['message'] = 'SomeError'

	return result

def insert_order(order_data):
	result={}
	try:
		selling_partner = Company.objects.get(id=order_data['selling_partner'])
		order_info = Order(
			order_date=timezone.now(), 
			order_amount=order_data['order_amount'],
			collect_money=order_data['collect_money'],
			subtract_amount=order_data['subtract_amount'],
			outstanding_amount=order_data['outstanding_amount'],
			description=order_data['description'])
		order_info.selling_partner=selling_partner
		order_info.save()
		result['message'] = 'success'
		result['data']=order_info
	except Company.DoesNotExist:
		result['message'] = 'Company DoesNotExist'
	except :# error 발생시 
		result['message'] = 'SomeError'
	
	return result

################################################################################
def order_form(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			new_order_amount=form.cleaned_data[order_amount]
	else:
		form = OrderForm()

#product detail view page
def product_detail(request, product_id):
	try:
		product_info = Product.objects.get(pk=product_id)
	except Product.DoesNotExist:
		raise Http404("Product does not exist")

	return render(request, 'testapp/product_detail.html', {'product_info': product_info})



def product_new(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = ProductForm()
	return render(request, 'testapp/product_form.html', {
		'form': form,
	})


def product_edit(request, product_id):
	post = get_object_or_404(Product, pk=product_id)

	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
	else:
		form = ProductForm(instance=post)
	
	return render(request, 'testapp/product_edit.html', {
		'form': form,
	})

