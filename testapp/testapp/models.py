from django.db import models

class Order(models.Model):
	order_date = models.DateTimeField('date ordered')
	selling_partner = models.IntegerField(default=0) 
	order_amount = models.IntegerField(default=0)
	collect_money = models.IntegerField(default=0) 
	subtract_amount = models.IntegerField(default=0) 
	outstanding_amount = models.IntegerField(default=0) 
	description = models.CharField(max_length=200,default=0)

class Order_item(models.Model):
	product_id = models.IntegerField(default=0) 
	unit_price = models.IntegerField(default=0)
	amount = models.IntegerField(default=0)
	grade = models.CharField(max_length=200,default=0)
	order_id = models.IntegerField(default=0)
	description = models.CharField(max_length=200,default=0)

class Product(models.Model):
	unit =  models.CharField(max_length=100,default=0)
	name =  models.CharField(max_length=100,default=0)
	description = models.CharField(max_length=200,default=0)
	price = models.IntegerField(default=0)
	question_text = models.CharField(max_length=200,default=0)



class company(models.Model):
	name =  models.CharField(max_length=100,default=0)
	call =  models.CharField(max_length=100,default=0)
	address = models.CharField(max_length=200,default=0)
	pic_name = models.CharField(max_length=200,default=0)
	description = models.CharField(max_length=200,default=0)
