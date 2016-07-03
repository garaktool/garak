from django.db import models
from django.utils.deconstruct import deconstructible

@deconstructible
class Company(models.Model):
	id = models.AutoField(primary_key=True)
	name =  models.CharField(max_length=100,default=0)
	call =  models.CharField(max_length=100,default=0)
	address = models.CharField(max_length=200,default=0)
	pic_name = models.CharField(max_length=200,default=0)
	description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'Company: ' + self.name 

@deconstructible
class Product(models.Model):
	id = models.AutoField(primary_key=True)
	unit =  models.CharField(max_length=100,default=0)
	name =  models.CharField(max_length=100,default=0)
	description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'Product: ' + self.name

@deconstructible
class Order(models.Model):
	id = models.AutoField(primary_key=True)
	order_date = models.DateTimeField('date ordered')
	selling_partner =  models.ForeignKey(Company) 
	order_amount = models.IntegerField(default=0)
	collect_money = models.IntegerField(default=0) 
	subtract_amount = models.IntegerField(default=0) 
	outstanding_amount = models.IntegerField(default=0) 
	description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'Order: ' + self.description

@deconstructible
class Order_item(models.Model):
	id = models.AutoField(primary_key=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE) 
	product = models.ForeignKey(Product)
	unit_price = models.IntegerField(default=0)
	amount = models.IntegerField(default=0)
	grade = models.CharField(max_length=200,default=0)
	description = models.CharField(max_length=200,default=0)
	
	def __unicode__(self):
		return 'Order_item: ' + self.product.name