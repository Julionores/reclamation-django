from django.contrib import admin

# Register your models here.

# Register your models here.

from .models import User

class UserAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('username', 'email','is_staff','is_superuser','date_edit','date_created','reclamation_object') # liste les champs que nous voulons sur l'affichage de la liste
    search_fields = ('username', 'email', 'reclamation_object')
    list_filter = ('date_edit','date_created',)
    readonly_fields = ('date_edit',)

admin.site.register(User, UserAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
