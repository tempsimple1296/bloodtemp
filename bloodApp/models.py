from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here.

class User(models.Model):	
	userName = models.CharField(max_length=50)
	userAge = models.IntegerField(default=18,max_length=2)
	userLoc = models.CharField(max_length=50)	
	userBloodGroup = models.CharField(max_length=3,validators=[RegexValidator(r'^(A|B|AB|O|a|b|ab|o)[+-]$','Enter A Valid Human BloodGroup..!!!')])
	time = models.DateTimeField('date published',default=timezone.now)
	def timeSet(self):
		return self.time.date == datetime.date.today()


