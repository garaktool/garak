from django.db import models
from django.forms import ModelForm
from django import forms
from .models import Store

class StoreForm(ModelForm):
	class Meta:
		model = Store
		#fields = '__all__'
		#fields = ['unit', 'price', 'description','question_text','name']

