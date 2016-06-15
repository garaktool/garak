from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Product

class ProductForm(ModelForm):
	class Meta:
		model = Product
		#fields = '__all__'
		fields = ['unit', 'price', 'description','question_text','name']

class OrderForm(ModelForm):
	order_amount = forms.IntegerField(label='Order amount')