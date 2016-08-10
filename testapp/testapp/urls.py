from django.conf.urls import patterns, include, url

from django.contrib import admin
from . import views, subpage_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
app_name = 'testapp'

##edit0810
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index, name='index'),
	url(r'^order$', views.order, name='order'),
	url(r'^home$', views.home, name='home'),
	url(r'^submit_order$', views.submit_order, name='submit_order'),
	url(r'^item_control$', subpage_views.item_control, name='item_control'),
	url(r'^grade_control$', subpage_views.grade_control, name='grade_control'),
	url(r'^unit_control$', subpage_views.unit_control, name='unit_control'),
	url(r'^store_control$', subpage_views.store_control, name='store_control'),
]