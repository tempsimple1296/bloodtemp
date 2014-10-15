from django.conf.urls import include, url
from django.contrib import admin
from bloodApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import social_auth
 

urlpatterns = [
    url(r'',include('social_auth.urls')),
    url(r'^$', views.home),
url(r'^RegisteredEntries/$',views.registered_entries),
        
url(r'^group/',views.groups),
    url(r'^count/',views.count),
    url(r'^home/',views.index),
    url(r'^register/',views.signin),
    url(r'^registerUser/',views.register),
#    url(r'complete/facebook/',views.register),
    #url(r'^profile/',views.profile),
    url(r'^admin/', include(admin.site.urls)),
    url('account-already-associated',views.CustomSocialAuthExceptionMiddleware),
    url(r'^account/error/',views.showError),
    url(r'^fbRegister',views.fbRegister),
    url(r'^am-I-Eligible/$',views.amIEligible),
    url(r'^termsAndCondition/$',views.termsAndCondition),
    url(r'^FAQ/$',views.FAQ),
    url(r'^whyBloodApp',views.whyBloodApp),
    #url(r'^features/',views.features),
    url(r'^logout/',views.logout),
    url(r'^aboutMe/',views.developer),
    url(r'^google37e4d89724d52b78.html/',views.webmaster),
    url(r'^prateek/sitemap',views.sitemap),
]

urlpatterns += staticfiles_urlpatterns()

