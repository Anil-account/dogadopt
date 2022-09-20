from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import *

# Create your views here.


def admin(request):
    return render(request, 'admin/admin.html')


def user(request):
    user = User.objects.exclude(username=request.user.username)
    context = {
        "all_users":user,
    }
    return render (request, 'admins/user.html',context)

