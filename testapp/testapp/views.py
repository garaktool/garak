from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils import timezone
from testapp.forms import ProductForm
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

def submit_order(request):
	response_data={}
	response_data['result'] = 'failed'
	if request.method == 'POST':
		if request.POST['order_pk']:
			try:
				order_info = Order.objects.get(pk=request.POST['order_pk'])
				order_info.order_date=timezone.now() 
				order_info.order_amount=request.POST['order_amount']
				order_info.collect_money=request.POST['collect_money']
				order_info.subtract_amount=request.POST['subtract_amount']
				order_info.outstanding_amount=request.POST['outstanding_amount']
				order_info.description=request.POST['description']
				order_info.save()
			except Order.DoesNotExist:
				response_data['result'] = 'Order DoesNotExist'
		else:
			order_info = Order(
				order_date=timezone.now(), 
				order_amount=request.POST['order_amount'],
				collect_money=request.POST['collect_money'],
				subtract_amount=request.POST['subtract_amount'],
				outstanding_amount=request.POST['outstanding_amount'],
				description=request.POST['description'])
			order_info.save()
			response_data['result'] = 'success'

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		response_data['result'] = 'method errorr(POST)'
		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)

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

