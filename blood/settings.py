"""
Django settings for blood project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jwsgn1)2jc6_bm6rhs3d558_#0bgsjxbut#fdry08(&0*(opv1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
#TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bloodApp',
    'social_auth',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
) 

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
'bloodApp.views.CustomSocialAuthExceptionMiddleware',
    )


GOOGLE_OAUTH2_CLIENT_ID = '802976274972-gva31epe6kcfnstlc7v9k8s6u1gtig3u.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'BpsbqwJma4qpfGpELwT3naoG'

FACEBOOK_APP_ID = '884234344938916'
FACEBOOK_API_SECRET = 'de9ee3c42f53d4d28284751e7e0b18f5'
SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

#FACEBOOK_EXTENDED_PERMISSIONS = ['email','user_about_me','user_birthday']
SOCIAL_AUTH_FACEBOOK_EXTENDED_PERMISSIONS = ['email', 'user_birthday']
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_birthday']


LOGIN_URL = '/account/login/'
#LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/account/error/'
LOGIN_REDIRECT_URL='/registerUser'

'''TEMPLATE_DIRS=(
'/home/prateek/blood/blood/templates',
)'''



ROOT_URLCONF = 'blood.urls'

WSGI_APPLICATION = 'blood.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
'''
import dj_database_url
DATABASES = { 'default' : dj_database_url.config()}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blood',
	'USER':'root',
	'PASSWORD':'mysql',
	'HOST':'localhost',
	'PORT':'3306',
    }
}

# Internationalization
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}



# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT= 'staticfiles'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
#'/home/prateek/blood/blood/templates/static')	
