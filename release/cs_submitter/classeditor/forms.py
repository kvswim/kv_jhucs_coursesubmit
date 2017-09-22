#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#Form for classeditor, essentially a clone of MainFormModelForm.
#Uses ModelForm to translate the model into a form, with which the view can edit.
from django import forms
from mainform.models import MainFormModel

class EditForm(forms.ModelForm):
	class Meta:
		model = MainFormModel