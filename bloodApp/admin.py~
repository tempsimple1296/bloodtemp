from django.contrib import admin
from bloodApp.models import User,Location

class UserAdmin(admin.ModelAdmin):
	fields=['userName','userAge','userLoc','userContact','userBloodGroup','time']

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Location)

