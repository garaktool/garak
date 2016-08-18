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

#edit0810 2
def item_control(request):
	result={'message':'success'}
	item_info={}
	#submit
	if request.method == 'POST':
		form_data = request.POST
		
		#update
		if form_data['item_id'] :
			try:
				item_unit_obj=Unit.objects.get(pk=form_data['item_unit_id'])
				item_info =Item.objects.get(pk=form_data['item_id'])
				item_info.item_name        =form_data['item_name']
				item_info.item_description =form_data['item_description']
				item_info.item_unit     =item_unit_obj
				item_info.item_code        =form_data['item_code']
				item_info.save()
			except Unit.DoesNotExist:
				result['message'] = 'Unit DoesNotExist'
			
			except Exception as e:# error �߻��� 
				result['message'] = 'item_update_error'
				print "#########" + e.message
			
		#insert
		else :
			try:
				item_unit_obj=Unit.objects.get(pk=form_data['item_unit_id'])
				item_code_row=Item.objects.get(item_code=form_data['item_code'])
				
				if item_code_row.item_id:
					result['message'] = 'Item Code aleady exist'

			except Item.DoesNotExist:
				item_info = Item( 
					item_name =form_data['item_name'],
					item_description =form_data['item_description'],
					item_unit =item_unit_obj,
					item_code=form_data['item_code'])
				item_info.save()

			except Unit.DoesNotExist:
				result['message'] = 'Unit DoesNotExist'
				
			except Exception as e:# error �߻��� 
				result['message'] = 'item_insert_error' + e.message
				print "@#@#@#@#" + e.message
				
			
	#item_view
	else :
		
		#edit item view
		if request.GET.get('item_id'):
			item_info =Item.objects.get(pk=request.GET.get('item_id'))
		#new item view
		else :
			# Generates a "SELECT MAX..." statement
			suggest_item_code=Item.objects.all().aggregate(Max('item_code'))
			suggest_item_code = suggest_item_code['item_code__max']+1
			item_info={'item_code':suggest_item_code}
	
	context = {'item_info': item_info, 'result':result['message']}
	return render(request, 'testapp/item_control.html', context)

def grade_control(request):
	 return render(request, 'testapp/grade_control.html')

def unit_control(request):
	 return render(request, 'testapp/unit_control.html')

def store_control(request):
	 return render(request, 'testapp/store_control.html')

################################################################################
