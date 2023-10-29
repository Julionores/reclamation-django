from django.shortcuts import render

# Create your views here.

from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import View

# from . import forms
  
