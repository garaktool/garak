from django.contrib.auth.models import User, Group
from django.db import models
from .models import Item, Order, Ordered_item, Store, Grade, Unit

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class StoreSerializer(serializers.HyperlinkedModelSerializer) :

    class Meta:
        model = Store
        fields = ('store_name','store_code','store_call','store_address','store_pic_name','store_description',)

class ItemSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Item
        fields = ('item_name',)

class GradeSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Grade
        fields = ('grade_name',)

class Ordered_itemSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Ordered_item
        fields = ('ordered_item_unit_price',)

class OrderSerializer(serializers.HyperlinkedModelSerializer) :
    order_store = StoreSerializer()
    ordered_item_set=Ordered_itemSerializer()
    #ordered_item_set = serializers.HyperlinkedIdentityField(view_name='ordered_item-list')

    class Meta:
        model = Order
        fields = ('order_notes','order_store','ordered_item_set',)
        #fields = '__all__'


