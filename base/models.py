from django.db import models

from django.db import models

class Agence(models.Model):
    agence_id = models.IntegerField(primary_key=True)
    agence_name = models.CharField(max_length=255)

class Agent(models.Model):
    agent_id = models.IntegerField(primary_key=True)
    agent_code = models.CharField(max_length=30, unique=True)
    agent_agence = models.ForeignKey(Agence, on_delete=models.CASCADE, related_name='agents')
    agent_name = models.CharField(max_length=255)
    agent_mail = models.CharField(max_length=255)

class ReclamationObject(models.Model):
    reclamation_object_name = models.CharField(max_length=255)

class Reclamation(models.Model):
    reclamation_reference = models.CharField(max_length=255, unique=True)
    reclamation_date = models.DateField(null=True, default=None)
    reclamation_firstname = models.CharField(max_length=255)
    reclamation_lastname = models.CharField(max_length=255)
    reclamation_adresse = models.CharField(max_length=255, null=True, default=None)
    reclamation_tel = models.CharField(max_length=255)
    reclamation_mail = models.CharField(max_length=255, null=True, default=None)
    reclamation_customer = models.BooleanField(default=False)
    reclamation_agence = models.ForeignKey(Agence, on_delete=models.CASCADE, null=True, default=None)
    reclamation_account_number = models.CharField(max_length=255, null=True, default=None)
    reclamation_object = models.ForeignKey(ReclamationObject, on_delete=models.CASCADE, null=True, default=None)
    reclamation_detail = models.TextField()
    reclamation_response = models.CharField(max_length=255, null=True, default=None)
    reclamation_rejected = models.BooleanField(default=False)
    reclamation_closed = models.BooleanField(default=False)
    reclamation_userassigned = models.IntegerField(null=True, default=None)
    reclamation_code_agent = models.CharField(max_length=255, default="")