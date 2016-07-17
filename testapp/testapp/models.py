from django.db import models


class Store(models.Model):
	store_id = models.AutoField(primary_key=True)
	store_name =  models.CharField(max_length=100,default=0)
	store_call =  models.CharField(max_length=100,default=0)
	store_address = models.CharField(max_length=200,default=0)
	store_pic_name = models.CharField(max_length=200,default=0)
	store_description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'Store: ' + self.store_name 

class Unit(models.Model):
	unit_id = models.AutoField(primary_key=True)
	unit_name =  models.CharField(max_length=100,default=0)
	unit_description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'unit: ' + self.unit_name

class Grade(models.Model):
	grade_id = models.AutoField(primary_key=True)
	grade_name =  models.CharField(max_length=100,default=0)
	grade_description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'grade: ' + self.grade_name

class Item(models.Model):
	item_id = models.AutoField(primary_key=True)
	item_unit = models.ForeignKey(Unit,on_delete=models.SET_DEFAULT, default=100000)
	item_name =  models.CharField(max_length=100,default=0)
	item_description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'item: ' + self.item_name

class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	order_date = models.DateTimeField('date ordered')
	order_store =  models.ForeignKey(Store,default=100000,on_delete=models.SET_DEFAULT) 
	order_total_amount = models.IntegerField(default=0)
	order_paid_amount = models.IntegerField(default=0) 
	order_discounted_amount = models.IntegerField(default=0) 
	order_outstanding_amount = models.IntegerField(default=0) # nonpaid
	order_notes = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'Order: ' + self.order_notes

class Ordered_item(models.Model):
	ordered_item_id = models.AutoField(primary_key=True)
	ordered_item_order = models.ForeignKey(Order, on_delete=models.CASCADE) 
	ordered_item_item = models.ForeignKey(Item,default=100000,on_delete=models.SET_DEFAULT)
	ordered_item_unit_price = models.IntegerField(default=0)
	ordered_item_qty = models.IntegerField(default=0)
	ordered_item_unit = models.ForeignKey(Unit,default=100000,on_delete=models.SET_DEFAULT)
	ordered_item_grade = models.ForeignKey(Grade,default=100000,on_delete=models.SET_DEFAULT)
	ordered_item_description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'Ordered_item: ' + self.ordered_item_description