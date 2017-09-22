#Kyle Verdeyen
#Independent Study, Summer 2017
#Joanne Selinski
#Model for the main form. This is the most important file in the project! Declare new fields here (among other places, read docs).
import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
# Create your models here.
CS_AREA_CHOICES = (
	('', 'n/a'),
	('ANALYSIS', 'Analysis'),
	('APPLICATIONS', 'Applications'),
	('SYSTEMS', 'Systems'),
	)
CS_FACULTY_CHOICES = (
('', 'Pick a faculty'),
('STAFF', 'Staff'),
('Ahmad, Yanif','Ahmad, Yanif'),
('Amir, Yair','Amir, Yair'),
('Arora, Raman','Arora, Raman'),
('Battle, Alexis','Battle, Alexis'),
('Braverman, Vladimir','Braverman, Vladimir'),
('Burns, Randal','Burns, Randal'),
('Dahbura, Anton','Dahbura, Anton'),
('Dinitz, Michael','Dinitz, Michael'),
('Drezde, Mark','Drezde, Mark'),
('Duh, Kevin','Duh, Kevin'),
('Eisner, Jason','Eisner, Jason'),
('Froehlich, Peter','Froehlich, Peter'),
('Green, Matthew','Green, Matthew'),
('Hager, Gregory','Hager, Gregory'),
('Hohenberger, Susan','Hohenberger, Susan'),
('Huang, Ryan (Peng)','Huang, Ryan (Peng)'),
('Jain, Abhishek','Jain, Abhishek'),
('Jin, Xin','Jin, Xin'),
('Kazanzides, Peter','Kazanzides, Peter'),
('Kazhdan, Michael','Kazhdan, Michael'),
('Koehn, Philipp','Koehn, Philipp'),
('Kosaraju, S. Rao','Kosaraju, S. Rao'),
('Langmead, Benjamin','Langmead, Benjamin'),
('Leonard, Simon','Leonard, Simon'),
('Li, Xin','Li, Xin'),
('Masson, Gerald','Masson, Gerald'),
('Miner More, Sara','Miner More, Sara'),
('Navab, Nassir','Navab, Nassir'),
('Reiter, Austin','Reiter, Austin'),
('Rubin, Aviel','Rubin, Aviel'),
('Salzberg, Steven','Salzberg, Steven'),
('Saria, Suchi','Saria, Suchi'),
('Schatz, Michael','Schatz, Michael'),
('Selinski, Joanne','Selinski, Joanne'),
('Shpitser, Ilya','Shpitser, Ilya'),
('Smith, Scott','Smith, Scott'),
('Szalay, Alex','Szalay, Alex'),
('Taylor, Rusell','Taylor, Rusell'),
('Terzis, Andreas','Terzis, Andreas'),
('Van Durme, Benjamin','Van Durme, Benjamin'),
('Yarowsky, David','Yarowsky, David'),
('Yuille, Alan','Yuille, Alan'),
)
COURSE_AREA_CHOICES = (
	('','n/a'),
	('H','H'),
	('E','E'),
	('Q','Q'),
	('NQ','NQ'),
	('EQ','EQ'),
	)
NUM_CREDITS_CHOICES = (
	('', '0'),
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	)
SEMESTER_CHOICES = (
	('', 'Pick a semester'),
	('F','Fall 2017'),
	('S', 'Spring 2018')
	)

class MainFormModel(models.Model):
	is_new_course = models.BooleanField()
	class_number = models.IntegerField()
	section_number = models.IntegerField()
	course_title = models.CharField(max_length=255)
	course_description = models.TextField()
	cs_area = models.CharField(max_length = 12, choices = CS_AREA_CHOICES, blank=True)
	course_instructor = models.CharField(max_length = 255, choices = CS_FACULTY_CHOICES, blank=False)
	start_time = models.TimeField()
	end_time = models.TimeField()
	is_monday = models.BooleanField()
	is_tuesday = models.BooleanField()
	is_wednesday = models.BooleanField()
	is_thursday = models.BooleanField()
	is_friday = models.BooleanField()
	semester = models.CharField(max_length = 12, choices = SEMESTER_CHOICES, blank=False)

	course_area = models.CharField(max_length = 4, choices = COURSE_AREA_CHOICES, blank=True)
	num_credits = models.CharField(max_length = 4, choices=NUM_CREDITS_CHOICES, blank=True)
	enrollment_limit = models.IntegerField()
	final_exam = models.BooleanField()
	

	#Todo: autocomplete in form, clone class, maybe last modified timestamp?

	def __str__(self):
		return self.course_title



