from django.shortcuts import render
import os
from django.shortcuts import render, redirect
from home.auth import admin_only
from home.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import *



    

@login_required
@admin_only
def user_display(request):
    all_user = User.objects.exclude(username=request.user.username)
    user_filter = UsernameFilter(request.GET, queryset=all_user)
    user_final = user_filter.qs
    context = {
        "all_users": user_final,
        "user_filter": user_filter
    }
    return render(request, 'admins/user.html', context)



# Create your views here.
@login_required
@admin_only
def admins(request):
    return render(request, 'admins/admin.html')

@login_required
@admin_only
def user_change_admin(request,username):
    user = User.objects.filter(username=username)
    user.update(is_staff=True)
    return redirect ('/admins/useradmin')


@login_required
@admin_only
def admin_change_user(request,username):
    user = User.objects.filter(username=username)
    user.update(is_staff=False)
    return redirect ('/admins/useradmin')


@login_required
@admin_only
def delete_user(request, user_id):
    user_data = User.objects.get(id=user_id)    
    user_data.delete()
    return redirect('/admins/useradmin')


def deletestory(request, story_id):
    story_data = Stories.objects.get(id=story_id)
    story_data.delete()
    return redirect('/admins/story')


def viewstory(request):
    story = Stories.objects.all()
    context = {
        "stories": story
    }
    return render(request, 'admins/story.html', context)



def deleteadopt(request,adopt_id):
    adopt = Adopt.objects.get(id=adopt_id)
    adopt.delete()
    return redirect('/admins/viewadapt')



def viewadopt(request):
    adopts = Adopt.objects.all()
    context = {
        "adopts": adopts
    }
    return render(request, 'admins/post.html', context)

    
