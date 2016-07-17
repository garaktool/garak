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
	url(r'^order$', views.order, name='order'),
	url(r'^submit_order$', views.submit_order, name='submit_order'),
]