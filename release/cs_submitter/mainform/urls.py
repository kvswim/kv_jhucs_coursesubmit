#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#URL config for mainform app, takes any site.com/form to index.html
from django.conf.urls import url
from .forms import MainFormModelForm
from . import views

app_name = 'mainform'
urlpatterns = [
	url(r'^$', views.index, name='form'),
]