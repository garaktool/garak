from django.db import models
from datetime import datetime 
from django.db.models import Max

class Store(models.Model):
	store_id = models.AutoField(primary_key=True)
	store_name =  models.CharField(max_length=100,default=0)
	store_code =  models.IntegerField(unique=True,default=None)
	store_call =  models.CharField(max_length=100,default=0)
	store_address = models.CharField(max_length=200,default=0)
	store_pic_name = models.CharField(max_length=200,default=0)
	store_description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'Store: ' + self.store_name 
	def save(self): 
		max_code_number=Store.objects.all().aggregate(Max('store_code'))
		self.store_code=max_code_number+1
		super(Store, self).save()


class Unit(models.Model):
	unit_id = models.AutoField(primary_key=True)
	unit_name =  models.CharField(max_length=100,default=0)
	unit_code =  models.IntegerField(unique=True,default=None)
	unit_description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'unit: ' + self.unit_name
	
	def save(self): 
		max_code_number=Unit.objects.all().aggregate(Max('unit_code'))
		self.unit_code=max_code_number+1
		super(Unit, self).save()



class Grade(models.Model):
	grade_id = models.AutoField(primary_key=True)
	grade_name =  models.CharField(max_length=100,default=0)
	grade_code =  models.IntegerField(unique=True,default=None)
	grade_description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'grade: ' + self.grade_name
	
	def save(self): 
		max_code_number=Grade.objects.all().aggregate(Max('grade_code'))
		self.grade_code=max_code_number+1
		super(Grade, self).save()



class Item(models.Model):
	item_id = models.AutoField(primary_key=True)
	item_unit = models.ForeignKey(Unit,on_delete=models.SET_DEFAULT, default=100000)
	item_name =  models.CharField(max_length=100,default=0)
	item_code =  models.IntegerField(unique=True,default=None)
	item_description = models.CharField(max_length=200,default=0)
	def __unicode__(self):
		return 'item: ' + self.item_name
	
	def save(self): 
		max_code_number=Item.objects.all().aggregate(Max('item_code'))
		if self.item_code <1:
			self.item_code=max_code_number+1
		super(Item, self).save()

class Adjustment(models.Model):
	adjustment_id = models.AutoField(primary_key=True)
	adjustment_date = models.DateTimeField('date adjusted',default=datetime.now())
	adjustment_bank = models.CharField(max_length=20,default=0)
	adjustment_type  = models.CharField(max_length=20,default=0)
	adjustment_total_amount = models.IntegerField(default=0) 
	adjustment_notes =  models.CharField(max_length=200,default=0)
	
	def __unicode__(self):
		return 'adjustment: ' + self.adjustment_notes

class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	order_date = models.DateTimeField('date ordered')
	order_store =  models.ForeignKey(Store,default=100000,on_delete=models.SET_DEFAULT) 
	order_total_amount = models.IntegerField(default=0)
	order_paid_amount = models.IntegerField(default=0) 
	order_discounted_amount = models.IntegerField(default=0) 
	order_outstanding_amount = models.IntegerField(default=0) # nonpaid
	order_notes = models.CharField(max_length=200,default=0)
	order_adjustment_id= models.IntegerField(default=0)
	order_adjustment_state = models.CharField(max_length=20,default=0)
	order_adjustment_type = models.CharField(max_length=20,default=0)
	order_adjustment_date = models.DateTimeField('date adjusted',default=datetime.now())
	def __unicode__(self):
		return 'Order: ' + self.order_notes
		#return '%s %s' % (self.first_name, self.order_notes)



class Ordered_item(models.Model):
	ordered_item_id = models.AutoField(primary_key=True)
	ordered_item_order = models.ForeignKey(Order, on_delete=models.CASCADE) 
	ordered_item_item = models.ForeignKey(Item,default=100000,on_delete=models.SET_DEFAULT)
	ordered_item_unit_price = models.IntegerField(default=0)
	ordered_item_qty = models.IntegerField(default=0)
	ordered_item_unit = models.ForeignKey(Unit,default=100000,on_delete=models.SET_DEFAULT)
	ordered_item_grade = models.ForeignKey(Grade,default=100000,on_delete=models.SET_DEFAULT)
	ordered_item_description = models.CharField(max_length=200,default=0)

	def _ordered_item_total_amount(self):
		c_t=self.ordered_item_qty * self.ordered_item_unit_price
		return c_t
	
	ordered_item_total_amount = property(_ordered_item_total_amount)

	def __unicode__(self):
		return 'Ordered_item: ' + self.ordered_item_description