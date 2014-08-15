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

ALL_LOCATIONS = (
	('Andhra Pradesh','Andhra Pradesh'),
	('Andaman and Nicobar Islands','Andaman and Nicobar Islands(UT)'),
	('Arunachal Pradesh','Arunachal Pradesh'),
	('Assam','Assam'),
	('Bihar','Bihar'),
	('Chandigarh','Chandigarh (UT)'),
	('Chhattisgarh','Chhattisgarh'),
	('Dadra and Nagar Haveli ','Dadra and Nagar Haveli (UT)'),
	('Daman and Diu ','Daman and Diu (UT)'),
	('Delhi','Delhi (UT)'),
	('Goa','Goa'),
	('Gujarat','Gujrat'),
	('Haryana','Haryana'),
	('Himachal Pradesh','Himachal Pradesh'),
	('Jammu and Kashmir','Jammu and Kashmir'),
	('Jharkhand','Jharkhand'),
	('Karnataka','Karnataka'),
	('Kerala','Kerala'),
	('Lakshadweep','Lakshadweep (UT)'),
	('Madhya Pradesh','Madhya Pradesh'),
	('Maharashtra','Maharashtra'),
	('Manipur','Manipur'),
	('Meghalya','Meghalya'),
	('Mizoram','Mizoram'),
	('Nagaland','Nagaland'),
	('Odisha','Odisha'),
	('Pondicherry','Pondicherry (UT)'),
	('Punjab','Punjab'),
	('Rajasthan','Rajasthan'),
	('Sikkim','Sikkim'),
	('Tanil Nadu','Tamil Nadu'),
	('Tripura','Tripura'),
	('Uttar Pradesh','Uttar Pradesh'),
	('Uttarakhand','Uttarakhand'),
	('West Bengal','West Bengal'),
)

class RegisterationForm(ModelForm):
	userBloodGroup=forms.ChoiceField(choices=MY_BLOOD_GROUP)
	userLoc=forms.ChoiceField(choices=ALL_LOCATIONS)
	class Meta:
		model=User
		#fields = 'userName','userAge','userBloodGroup','userLoc','time'
		fields = '__all__'		
		widgets = {
            		'userName': forms.TextInput(attrs={'class': 'form-control '}),
        		'userAge': forms.TextInput(attrs={'class': 'form-control'}),
			'userBloodGroup': forms.TextInput(attrs={'class': 'form-control'}),
			'userLoc': forms.TextInput(attrs={'class': 'form-control'}),
			'time': forms.TextInput(attrs={'type':'hidden'}),#{'class': 'form-control'}),#,'disabled':''}),
			'userContact': forms.TextInput(attrs={'type':'hidden'}),			
		}

