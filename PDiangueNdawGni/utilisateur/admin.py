from django.contrib import admin
from utilisateur.models import *

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass