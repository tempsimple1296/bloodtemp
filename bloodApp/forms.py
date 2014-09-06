from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from bloodApp.models import User
from django.utils.translation import ugettext_lazy as _

MY_BLOOD_GROUP = (
	('O+','O+'),
	('O-','O-'),
	('A+','A+'),
	('A-','A-'),
	('B+','B+'),
	('B-','B-'),
	('AB+','AB+'),
	('AB-','AB-'),
)

class RegisterationForm(ModelForm):
	userBloodGroup=forms.ChoiceField(choices=MY_BLOOD_GROUP)
	#userLoc=forms.ChoiceField(choices=ALL_LOCATIONS)
	class Meta:
		model=User
		#fields = 'userName','userAge','userBloodGroup','userLoc','time'
		fields = '__all__'		
		widgets = {
            		'userName': forms.TextInput(attrs={'class': 'form-control '}),
        		'userAge': forms.TextInput(attrs={'class': 'form-control'}),
			'userBloodGroup': forms.TextInput(attrs={'class': 'form-control'}),
			'userLoc': forms.TextInput(attrs={'id':'pac-input','class':'form-control'}),
#'class': 'form-control'}),
			'time': forms.TextInput(attrs={'type':'hidden'}),#{'class': 'form-control'}),#,'disabled':''}),
			'userContact': forms.TextInput(attrs={'type':'hidden'}),			
		}

	error_messages = {
            'userContact': {
                'unique': _("This id's already taken"),
            },
	}
