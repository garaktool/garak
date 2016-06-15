from django.contrib import admin

from .models import Product
from .models import Company
from .models import Order_item
from .models import Order
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Order_item)
admin.site.register(Order)
