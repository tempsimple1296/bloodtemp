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
 
class CustomSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_redirect_uri(self, request, exception):
        if isinstance(exception, AuthAlreadyAssociated):
            return HttpResponse('Sorry Something Went Wrong')
        else:
            return super(CustomSocialAuthExceptionMiddleware, self)\
                                 .get_redirect_uri(request, exception)

def logout(request):
	request.session.flush()
	request.session.clear()
	return HttpResponseRedirect('/')

def signin(request):
	print '-----in signin(request)-----'
	if (request.session.keys()):			
		return HttpResponseRedirect('/registerUser')	
	print 'sign in called'
	return render_to_response('signin.html')
	
'''def completeGoogleAuth(request):
	return HttpResponse("You Have Successfully Authorized with Google")
'''
def amIEligible(request):
	return render_to_response('whoCanDonate.html')	

def count(request):
	if(request.POST):
		print request
		f=[]
		index=0
		blood=["blood"]
		bloodGroup=['O+','O-','A+','A-','B+','B-','AB+','AB-']
		#print request
		#bloodGroup = request.POST['group']
		loc=request.POST['loc']		
		for bg in bloodGroup: 
			f.append(User.objects.filter(userLoc=loc).filter(userBloodGroup=bg).count())
		_max=f[0]
		for i in xrange(0,len(f)):
			if(f[i]==0):
				if(i==len(f)-1):
					return render_to_response('count.html',{'groupCount':f,'major':_max,'majorbloodGroup':"No One Registered yet..!!!"})
			else:
				break

		for i in xrange(1,len(f)):
			if(f[i]>_max):
				_max=f[i]
				index=i
		major=[]
		major.append(index)
		maximum = f[index]
		for i in xrange(index+1,len(f)):
			if(f[i]==maximum):
				major.append(i)
				
		for i in xrange(0,len(major)):
			major[i]=bloodGroup[major[i]]
		
		return render_to_response('count.html',{'groupCount':f,'major':_max,'majorbloodGroup':major})
	return HttpResponse("Sorry the Page You Requested Does Not Exist...!!")	
				
def groups(req):
	bloodGroup=""
	loc=""
	if(req.POST):
		bloodGroup = req.POST['group']
		loc=req.POST['loc']
		#print "bloodGroup-->",bloodGroup
		#print "loc --> ",loc		
		#loc=req.POST['input-pac']		
		if((bloodGroup and loc)):
			f=User.objects.filter(userBloodGroup=bloodGroup).filter(userLoc=loc)
		elif(bloodGroup=="" and loc==""):
			f=User.objects.all()
		else:
			if(loc==""):
				f=User.objects.filter(userBloodGroup=bloodGroup)
			else: 				 
				f=User.objects.filter(userLoc=loc)
		if(not (f)):
			return HttpResponse("No OneRegistered Yet ..!!!")
		return render_to_response('result.html',{'users':f})		
	else:
		#print 'No req.post called...!!!!!'    		
		return render_to_response('result.html')


def listAll(request):
	f=User.objects.all()
	#if request.method=="GET":
	#	print 'Get....'
	#f = User.objects.filter(userBloodGroup="o+")
	template = loader.get_template("list.html")
    	data = RequestContext(request, {'users':f})
    	return HttpResponse(template.render(data))
	
def whyBloodApp(request):
	return render_to_response('whyBloodApp.html')

def FAQ(request):
	return render_to_response('FAQ.html')

def termsAndCondition(request):
	return render_to_response('termsAndCondition.html')


def BloodGroupOrdered(request,group):#,BloodGroup):
	print group
	return HttpResponse('Hehehe got you now..!!!')#render_to_response('bloodgroup.html')

def profile(request):
	return HttpResponse(request)

def home(request):
	return render_to_response('home.html')

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
	
	#print '------------------'
	#print request.method
	#print '------------------'
	#print request
	#print "############################"
	if request.method=='POST':
		form = RegisterationForm(request.POST)
		print form		
		#form.fields['userContact'].initial = json_data["link"]
        #print form
		if form.is_valid():		
			'''print form.cleaned_data['userName']			
			print form.cleaned_data['userAge']			
			print form.cleaned_data['userBloodGroup']			
			print form.cleaned_data['userContact']			
			print form.cleaned_data['userLoc']			
			print form.cleaned_data['time']			
			'''	
			if(((int(form.cleaned_data['userAge'])<18))and(int(form.cleaned_data['userAge'])>60)):
				context = {'age_error':''}
				return render_to_response('age_error.html',context,context_instance=RequestContext(request))	
			entry = form.save()
			request.session.flush()
			return HttpResponseRedirect('/listUsers')
		else:
			#print form.fields['userContact'].initial
			#print form.fields['userName'].initial
			print 'form not valid'
			context = {'form': form.errors}
			request.session.flush()
			return render_to_response('error.html',context,context_instance=RequestContext(request))
			
	else:
		if (not(request.session.keys())):			
			return HttpResponseRedirect('/register')		
		else:
			#print "Provider--->"
			#print request
			form = RegisterationForm()
			context = {'form':form}
			provider = request.session.get('social_auth_last_login_backend')
			if(not(provider)):
				request.session.flush()
				return HttpResponseRedirect('/')
			print '##############################'
			print 'session'
			lists=request.session.keys()
			#print lists 
            		
                
			#for item in lists:
			#	print item,"-->",request.session.get(item)
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
			print 'JSON_DATA',json_data			
			if(not('link' in json_data)):
                		request.session.flush()
                		return render_to_response('noGooglePlus.html')	
			form.fields['userName'].initial = json_data["name"]
			form.fields['userContact'].initial = json_data["link"]
			print data 	
			print form.fields['userContact'].initial 	
			#a=json.loads(instance.tokens)
			#_id = user_social_auth.get(provider='facebook').uid
			#_id = UserSocialAuth.objects.filter(provider='facebook')
			#_id=UserSocialAuth.objects.all()
			print '----------------------------------------'		
			#pprint(instance.tokens)	
	return render_to_response('register.html',context,context_instance=RequestContext(request))	

def showError(request):
	message="Sorry Something Went Wrong"
	return HttpResponse(message)

def index(request):
	return render_to_response('index.html')

def group_blood(request, bloodgroup):
	user_list = User.objects.filter(userBloodGroup=bloodgroup)
	return render_to_response('list.html',{'users':user_list})

def features(request):
	return render_to_response('')

