from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from base.models import ReclamationObject

class User(AbstractUser):

    reclamation_object = models.ForeignKey(ReclamationObject, on_delete=models.CASCADE, null=True, default=None)
    code = models.CharField(max_length=128, unique=True)
    date_edit = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
