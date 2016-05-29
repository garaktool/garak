from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse
from testapp.forms import ProductForm
from .models import Product


class ProductDetailView(generic.DetailView):
	model = Product
	template_name = 'testapp/product_detail.html'

class ProductListView(generic.ListView):
	model = Product
	template_name = 'testapp/product_list.html'
	context_object_name = 'latest_product_list'
	def get_queryset(self):
		return Product.objects.order_by('-pub_date')[:5]

#test page
def hello(request):
    return HttpResponse("Hello world")

def index(request):
    latest_product_list = Product.objects.order_by('-pub_date')[:5]
    context = {'latest_product_list': latest_product_list} 
    return render(request, 'testapp/index.html', context)


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

