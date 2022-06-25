from django.contrib import admin
from user.models import Profile
 
 
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id","user","name","address","pincode","mobile"]
 
admin.site.register(Profile,ProfileAdmin)
