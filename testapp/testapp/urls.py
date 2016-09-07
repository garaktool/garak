from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
<<<<<<< HEAD
from .models import Item, Order, Ordered_item, Store, Grade, Unit
from django.contrib import admin
from . import views, subpage_views, submit_views, restapi_views
=======
from django.contrib import admin
from . import views, subpage_views, submit_views
>>>>>>> fcc0b402eb783538a8872d700c041dcf2e64d8c0
from rest_framework import routers, serializers, viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
<<<<<<< HEAD
router.register(r'api_users', restapi_views.UserViewSet)
router.register(r'api_groups', restapi_views.GroupViewSet)
router.register(r'api_orders', restapi_views.OrderViewSet)
router.register(r'api_items', restapi_views.OrderViewSet)
router.register(r'api_grades', restapi_views.OrderViewSet)
router.register(r'api_ordered_items', restapi_views.OrderViewSet)
router.register(r'api_stores', restapi_views.OrderViewSet)
=======
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
>>>>>>> fcc0b402eb783538a8872d700c041dcf2e64d8c0

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
app_name = 'testapp'

<<<<<<< HEAD
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.home, name='home'),
=======
##edit0810 2
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.home, name='home'),
	url(r'^order$', views.order, name='order'),
>>>>>>> fcc0b402eb783538a8872d700c041dcf2e64d8c0
	url(r'^home$', views.home, name='home'),
	url(r'^submit_order$', views.submit_order, name='submit_order'),
	url(r'^submit_page$', submit_views.submit_page, name='submit_page'),
	url(r'^submit_store$', submit_views.submit_store, name='submit_store'),
	url(r'^item_control$', subpage_views.item_control, name='item_control'),
	url(r'^grade_control$', subpage_views.grade_control, name='grade_control'),
	url(r'^unit_control$', subpage_views.unit_control, name='unit_control'),
	url(r'^store_control$', subpage_views.store_control, name='store_control'),
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]