#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#View for table page. Takes all objects from db and passes it to table.html
from django.shortcuts import render, render_to_response
from mainform.models import MainFormModel

# Create your views here.
def table(request):
	return render_to_response('table.html', {'classes' : MainFormModel.objects.all()})