from django.contrib import admin
from utilisateur.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

class UserResource(resources.ModelResource):

    class Meta:
        model = User


class UserAdmin(ImportExportModelAdmin):
    readonly_fields = ('date_joined',)
    list_display = ('email', )
    resource_class = UserResource

admin.site.register(User)