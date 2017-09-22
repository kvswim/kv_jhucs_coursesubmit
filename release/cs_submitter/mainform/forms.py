#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#Form for the mainform app. Uses ModelForm to translate the model into a form that the site can use to submit an object to the db.
from django import forms
from .models import MainFormModel

class MainFormModelForm(forms.ModelForm):
	class Meta:
		model = MainFormModel
		fields = (
			'is_new_course',
			'class_number', 
			'section_number',
			'course_title', 
			'course_description', 
			'cs_area', 
			'course_instructor', 
			'start_time', 
			'end_time', 
			'is_monday', 
			'is_tuesday',
			'is_wednesday',
			'is_thursday',
			'is_friday',
			'semester',

			'course_area',
			'num_credits',
			'enrollment_limit',
			'final_exam',
			)
		widgets = {
			'semester' : forms.RadioSelect(), #%I:%M %p
			'start_time': forms.TimeInput(format='%I:%M %p'),
			'end_time' : forms.TimeInput(format='%I:%M %p'),
		}
		labels = {
			'is_new_course':'Is this a new course',
			'class_number':'Class number (EN.601.XXX)',
			'section_number':'Section number (EN.601.000 (XX))',
			'cs_area':'CS Area',
			'start_time':'Start time (HH:MM AM/PM)',
			'end_time':'End time (HH:MM AM/PM)',
			'is_monday':'Monday',
			'is_tuesday':'Tuesday',
			'is_wednesday':'Wednesday',
			'is_thursday':'Thursday',
			'is_friday':'Friday',
			'num_credits':'Number of credits',
			'final_exam':'Final exam period',
		}