#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#URL configuration for the homepage 'app', any blank site.com/ will trigger this homepage
from django.conf.urls import url
from . import views

app_name = 'homepage'
urlpatterns = [
	url(r'^$', views.index, name='homepage'),
]