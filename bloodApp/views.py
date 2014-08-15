from django.shortcuts import *
from django.http import *
from models import User
from django.template import RequestContext
from forms import RegisterationForm
from social_auth.models import UserSocialAuth
import json
from pprint import pprint
from django.shortcuts import redirect
from urllib import * 
from social_auth.middleware import SocialAuthExceptionMiddleware
from social_auth.exceptions import AuthAlreadyAssociated
 
<<<<<<< HEAD
=======
 
>>>>>>> 48a1e4ad6832f87df8c6f5eaa3f526237172f429
class CustomSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_redirect_uri(self, request, exception):
        if isinstance(exception, AuthAlreadyAssociated):
            return HttpResponse('Sorry Something Went Wrong')
        else:
            return super(CustomSocialAuthExceptionMiddleware, self)\
                                 .get_redirect_uri(request, exception)
def signin(request):
	return render_to_response('signin.html')
<<<<<<< HEAD
	
'''def completeGoogleAuth(request):
	return HttpResponse("You Have Successfully Authorized with Google")
'''
=======

def completeGoogleAuth(request):
	return HttpResponse("You Have Successfully Authorized with Google")

>>>>>>> 48a1e4ad6832f87df8c6f5eaa3f526237172f429
def count(request):
	if(request.POST):
		print request
		f=[]
		blood=["blood"]
		bloodGroup=['O+','O-','A+','A-','B+','B-','AB+','AB-']
		#print request
		#bloodGroup = request.POST['group']
		loc=request.POST['loc']		
		for bg in bloodGroup: 
			f.append(User.objects.filter(userLoc=loc).filter(userBloodGroup=bg).count())
		_max=f[0]
		index=0
		for i in xrange(1,len(f)):
			if(f[i]>_max):
				_max=f[i]
				index=i

		return render_to_response('count.html',{'groupCount':f,'major':_max,'majorbloodGroup':bloodGroup[index]})		
	return HttpResponse("Sorry the Page You Requested Does Not Exist...!!")	
				
def groups(req):
	bloodGroup=""
	loc=""
	if(req.POST):
		bloodGroup = req.POST['group']
		loc=req.POST['loc']		
		if((bloodGroup and loc)):
			f=User.objects.filter(userBloodGroup=bloodGroup).filter(userLoc=loc)
		elif(bloodGroup=="" and loc==""):
			f=User.objects.all()
		else:
			if(loc==""):
				f=User.objects.filter(userBloodGroup=bloodGroup)
			else: 				 
				f=User.objects.filter(userLoc=loc)
		
		return render_to_response('result.html',{'users':f})		
	else:
    		return render_to_response('result.html')


def listAll(request):
	f=User.objects.all()
<<<<<<< HEAD
	#if request.method=="GET":
	#	print 'Get....'
=======
	if request.method=="GET":
		print 'Get....'
>>>>>>> 48a1e4ad6832f87df8c6f5eaa3f526237172f429
	#f = User.objects.filter(userBloodGroup="o+")
	template = loader.get_template("list.html")
    	data = RequestContext(request, {'users':f})
    	return HttpResponse(template.render(data))
#	return HttpResponse(render(request, "blog/index.html", {'articles':[article]}))
	
def BloodGroupOrdered(request,group):#,BloodGroup):
	print group
	return HttpResponse('Hehehe got you now..!!!')#render_to_response('bloodgroup.html')

def profile(request):
	return HttpResponse(request)

def home(request):
	return render_to_response('sexy.html')

def fbRegister(request):
	form={}
	if request.method=='POST':
		form = RegisterationForm(request.POST)
		if form.is_valid():				
			entry = form.save()
			return HttpResponseRedirect('/listUsers')

def register(request):
	form = {}
	context = {}
<<<<<<< HEAD
		
	print '------------------'
	print request.method
	print '------------------'
	#print request
	print "############################"
	if request.method=='POST':
		form = RegisterationForm(request.POST)
		print form		
		#form.fields['userContact'].initial = json_data["link"]
#		print form
		if form.is_valid():		
			'''print form.cleaned_data['userName']			
=======
	if request.method=='POST':
		form = RegisterationForm(request.POST)
		#form.fields['userContact'].initial = json_data["link"]
		print form
		if form.is_valid():		
			print form.cleaned_data['userName']			
>>>>>>> 48a1e4ad6832f87df8c6f5eaa3f526237172f429
			print form.cleaned_data['userAge']			
			print form.cleaned_data['userBloodGroup']			
			print form.cleaned_data['userContact']			
			print form.cleaned_data['userLoc']			
			print form.cleaned_data['time']			
<<<<<<< HEAD
			'''	
			entry = form.save()
			return HttpResponseRedirect('/listUsers')
		else:
			#print form.fields['userContact'].initial
			#print form.fields['userName'].initial
			print 'form not valid'
	else:
		'''print 'length',len(request.session.keys())
		for item in request.session.keys():
			print item,"-->",request.session.get(item)
		'''
		
		#if(len(request.session.keys())==0):
		if (not(request.session.keys())):			
			return HttpResponseRedirect('/register')		
	#if request.method=='GET':
			
		else:
			#print "Provider--->"
			#print request
			
			form = RegisterationForm()
			context = {'form':form}
			provider = request.session.get('social_auth_last_login_backend')
		
			print "Current Provider --> ",provider
			print '##############################'
			print 'session'
			lists=request.session.keys()
			for item in lists:
				print item,"-->",request.session.get(item)
			#if(provider=='facebook')
			#id_index = UserSocialAuth.objects.filter(provider='facebook').count()
			instance = UserSocialAuth.objects.filter(provider=request.session.get('social_auth_last_login_backend')).get(user_id=request.session.get('_auth_user_id'))
#id_index)	
			#json parsing	
			a = json.dumps(instance.tokens)
			token = json.loads(a)["access_token"]
			print "token --> ",token
			if(provider == "google-oauth2"):
				data=urlopen("https://www.googleapis.com/oauth2/v1/userinfo?access_token="+token).read()			
			elif(provider == "facebook"):
				data=urlopen("https://graph.facebook.com/me?access_token="+token).read()
			json_data = json.loads(data)
			form.fields['userName'].initial = json_data["name"]
			form.fields['userContact'].initial = json_data["link"] 	
			print form.fields['userContact'].initial 	
			#a=json.loads(instance.tokens)
			#_id = user_social_auth.get(provider='facebook').uid
		#	_id = UserSocialAuth.objects.filter(provider='facebook')
			#_id=UserSocialAuth.objects.all()
			print '----------------------------------------'		
			#pprint(instance.tokens)	
=======
				
			entry = form.save()
			return HttpResponseRedirect('/listUsers')
		else:
			print 'form not valid'
	if request.method=='GET':
		form = RegisterationForm()

	context = {'form':form}
	
	id_index = UserSocialAuth.objects.filter(provider='facebook').count()
	instance = UserSocialAuth.objects.filter(provider='facebook').get(id=id_index)	
	#json parsing	
	a = json.dumps(instance.tokens)
	token = json.loads(a)["access_token"]
	data=urlopen("https://graph.facebook.com/me?access_token="+token).read()
	#print '---------------------------------------'
	#print 'json wala email--->',json.loads(data)["email"]	
	#print '---------------------------------------'
	#print '------------Birthday--------------'
	#print json.loads(data)["birthday"]
	json_data = json.loads(data)
	form.fields['userName'].initial = json_data["name"]
	form.fields['userContact'].initial = json_data["link"] 	
	print form.fields['userContact'].initial 	
	#a=json.loads(instance.tokens)
	#_id = user_social_auth.get(provider='facebook').uid
#	_id = UserSocialAuth.objects.filter(provider='facebook')
	#_id=UserSocialAuth.objects.all()
	print '----------------------------------------'		
	#pprint(instance.tokens)	
>>>>>>> 48a1e4ad6832f87df8c6f5eaa3f526237172f429
	return render_to_response('register.html',context,context_instance=RequestContext(request))	

def showError(request):
	message="Sorry Something Went Wrong"
	return HttpResponse(message)

def index(request):
	return render_to_response('index.html')

def group_blood(request, bloodgroup):
	user_list = User.objects.filter(userBloodGroup=bloodgroup)
	return render_to_response('list.html',{'users':user_list})
<<<<<<< HEAD

=======
>>>>>>> 48a1e4ad6832f87df8c6f5eaa3f526237172f429
