from django.conf.urls import patterns, include, url

from django.contrib import admin
from . import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
app_name = 'testapp'

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index, name='index'),
	url(r'^product/(?P<product_id>[0-9]+)/$', views.product_detail, name='product_detail'),
	url(r'^order$', views.order, name='order'),
	url(r'^submit_order$', views.submit_order, name='submit_order'),
	url(r'^product_list/$',  views.ProductListView.as_view(), name='product_list'),
	url(r'^product_new/(?P<product_id>[0-9]+)/$', views.product_new, name='product_new'),
	url(r'^product_edit/(?P<product_id>[0-9]+)/$', views.product_edit, name='product_edit')
]