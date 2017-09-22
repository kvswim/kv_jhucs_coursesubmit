#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#Views for the classeditor, uses UpdateView to copy over the MainFormModel into something that can be edited.
from django.urls import reverse
from mainform.models import MainFormModel
from django.views.generic.edit import UpdateView
# Create your views here.

class ClassUpdate(UpdateView):
	model = MainFormModel
	fields = ['is_new_course',
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
			]
	template_name_suffix = '_update_form'
	def get_success_url(self):
		return reverse('table:table')