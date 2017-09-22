#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#View for homepage. Renders index.html for any request.
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
def index(request):
	return render_to_response('homepage/index.html')
