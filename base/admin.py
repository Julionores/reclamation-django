from django.contrib import admin

from base.models import Agence, Agent, Reclamation, ReclamationObject

class AgenceAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('agence_id','agence_name')
    search_fields = ('agence_name',)
    list_filter = ('agence_name',)
    readonly_fields = ('agence_id',)
    

admin.site.register(Agence, AgenceAdmin) 

class AgentAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('agent_code','agent_agence', 'agent_name', 'agent_mail')
    search_fields = ('agent_code','agent_agence', 'agent_name')
    list_filter = ('agent_name','agent_name')
    readonly_fields = ('agent_id',)
    

admin.site.register(Agent, AgentAdmin)

class ReclamationAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('reclamation_reference','reclamation_date', 'reclamation_firstname', 'reclamation_lastname', 'reclamation_adresse', 'reclamation_tel', 'reclamation_mail', 'reclamation_customer', 'reclamation_agence', 'reclamation_account_number', 'reclamation_object', 'reclamation_detail', 'reclamation_response', 'reclamation_rejected', 'reclamation_closed', 'reclamation_userassigned', 'reclamation_code_agent')
    search_fields = ('reclamation_reference','reclamation_firstname', 'reclamation_lastname', 'reclamation_adresse', 'reclamation_tel', 'reclamation_mail', 'reclamation_customer', 'reclamation_agence', 'reclamation_account_number', 'reclamation_object', 'reclamation_detail', 'reclamation_response', 'reclamation_rejected', 'reclamation_closed', 'reclamation_userassigned', 'reclamation_code_agent')
    list_filter = ('reclamation_reference','reclamation_agence')
    readonly_fields = ('reclamation_userassigned',)
    

admin.site.register(Reclamation, ReclamationAdmin)

class ReclamationObjectAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('reclamation_object_name',)
    search_fields = ('reclamation_object_name',)
    list_filter = ('reclamation_object_name',)
    

admin.site.register(ReclamationObject, ReclamationObjectAdmin)