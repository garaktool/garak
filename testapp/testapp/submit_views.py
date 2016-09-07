# -*- coding: utf-8 -*-
###
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Max,Sum
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import transaction
import datetime, time
from django.core.paginator import Paginator
from common_func import getInfo

from datetime import timedelta
import sys, traceback

from .models import Item, Order, Ordered_item, Store, Grade, Unit
import json

def submit_store(request):
	order_info = []
	global_value = {}
	response_data = {}
	from_data = json.loads(request.body)
	store_info = Store.objects.get(store_code=from_data['store_code'])

	order_info = Order.objects.filter(order_store=store_info)
	order_info = order_info.filter(order_adjustment_state='complete').aggregate(Sum('order_outstanding_amount'))
	response_data['global_total_outstanding'] = order_info
	#print order_info

	return HttpResponse(
		json.dumps(response_data),
		content_type="application/json"
	)

def submit_page(request):
	order_info = []
	global_value = {}
	response_data = {}
	from_data = json.loads(request.body)

	order_info = Order.objects.all()
	if from_data.get('search_store', False):
		#order_info = order_info.filter(order_store__store_name__contains=from_data['search_store'])
		search_store_code_string = getInfo().get_code(request.GET['search_store'])
		search_store_code_int = int(search_store_code_string)
		order_info = order_info.filter(order_store__store_code__contains=search_store_code_int)

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
		response_data['next_page'] = True
	else :
		response_data['next_page'] =False

	response_data['max_page'] =paginator.count

	return HttpResponse(
		json.dumps(response_data),
		content_type="application/json"
	)



################################################################################
