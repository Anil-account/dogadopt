from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from django.db import models
from .models import *



class CreateUserForm(UserCreationForm):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    class Meta:   
        model = User
        fields = ['first_name', 'last_name','username','email','password1','password2']

