#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#View for the mainform. Very basic validation checks. 
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from .forms import MainFormModelForm
from django.urls import reverse
# Create your views here.
def index(request):
	if request.method == "POST":
		form = MainFormModelForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.save()
			return redirect('/table')
	else:
		form = MainFormModelForm()
	return render(request, 'form/index.html', {'form' : form})
	#return reverse('table:table')		
