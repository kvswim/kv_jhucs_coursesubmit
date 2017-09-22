#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#URL patterns for table page. site.com/table 
from django.conf.urls import url
from . import views

app_name = 'table'
urlpatterns = [
	url(r'^$', views.table, name='table'),
]