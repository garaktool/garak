from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from django.contrib import admin
from . import views, subpage_views, submit_views
from rest_framework import routers, serializers, viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
app_name = 'testapp'

##edit0810 2
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.home, name='home'),
	url(r'^order$', views.order, name='order'),
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