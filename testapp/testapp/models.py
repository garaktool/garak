from django.db import models


class Product(models.Model):
	unit =  models.CharField(max_length=100,default=0)
	price = models.IntegerField(default=0)
	description = models.CharField(max_length=200,default=0)
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	name =  models.CharField(max_length=100,default=0)
	

class Order(models.Model):
	order_number = models.IntegerField(default=0)
	order_date = models.DateTimeField('date ordered')
	product_id = models.IntegerField(default=0) 
	description = models.CharField(max_length=200,default=0)

