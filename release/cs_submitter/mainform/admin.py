#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#Registers mainform into the admin site
from django.contrib import admin
from .models import MainFormModel
# Register your models here.
admin.site.register(MainFormModel)