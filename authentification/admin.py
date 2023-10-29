from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# Register your models here.

from .models import User

class CustomUserAdmin(UserAdmin):  # nous insérons ces deux lignes..

    add_fieldsets = UserAdmin.add_fieldsets + ( (None, {'fields': ('code','reclamation_object')}), ) 
    fieldsets = UserAdmin.fieldsets + ( (None, {'fields': ('code', 'reclamation_object')}), )

    list_display = ('username', 'email','is_staff','is_superuser','date_edit','date_created','reclamation_object') # liste les champs que nous voulons sur l'affichage de la liste
    search_fields = ('username', 'email', 'reclamation_object')
    list_filter = ('date_edit','date_created',)
    readonly_fields = ('date_edit',)

# admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
