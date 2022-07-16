from django.contrib import admin
from .models import TourApi, User

# Register your models here.
class TourApiAdmin(admin.ModelAdmin):
    list_display= ('title', 'contentid', 'firstimage', 'firstimage1', 'addr1', 'overview')

class UserAdmin(admin.ModelAdmin):
    list_display= ('username', 'email', 'password')

admin.site.register(User, UserAdmin)
admin.site.register(TourApi, TourApiAdmin) 

