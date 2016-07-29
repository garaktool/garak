from django.contrib import admin

from .models import Item
from .models import Store
from .models import Ordered_item
from .models import Adjustment
from .models import Order
from .models import Unit
from .models import Grade

admin.site.register(Item)
admin.site.register(Store)
admin.site.register(Ordered_item)
admin.site.register(Adjustment)
admin.site.register(Order)
admin.site.register(Unit)
admin.site.register(Grade)
