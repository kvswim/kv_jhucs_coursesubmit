#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#URL configuration for the classeditor app, anything with /edit/x will be sent to ClassUpdate view
from django.conf.urls import url
from .views import ClassUpdate

app_name = 'classeditor'
urlpatterns = [
	url(r'^(?P<pk>[\w-]+)$', ClassUpdate.as_view(), {}, name='classeditor'),
]