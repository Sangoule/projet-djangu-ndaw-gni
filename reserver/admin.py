from django.contrib import admin
from reserver.models import *

@admin.register(Compagnie)
class CompagnieAdmin(admin.ModelAdmin):
    pass
@admin.register(Vol)
class VolAdmin(admin.ModelAdmin):
    pass
@admin.register(Trajet)
class TrajetAdmin(admin.ModelAdmin):
    pass