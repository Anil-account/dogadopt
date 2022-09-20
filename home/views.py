from django.shortcuts import render,redirect
from .forms import CreateUserForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .auth import *
from .forms import CreateUserForm
from .models import *

# Create your views here.
def story(request):
    stories = Stories.objects.all()
    context = {
        "stories": stories
    }
    return render(request, 'home/story.html', context)

@user_only
def pet(request):
    return render(request, 'home/userPetProfile.html')



@user_only
def main(request):
    return render(request, 'home/main.html')

@user_only
def shop(request):
    return render(request, 'home/adopt.html')

@user_only
def about(request):
    return render(request, 'home/about.html')

@user_only
def adapt(request):
    pet_detail = Adopt.objects.all()
    print(pet_detail.count())
    context = {
        "all_pets": pet_detail
    }
    return render(request,'home/adopt.html', context)

@user_only
def pet_details(request, pet_id):
    pet = Adopt.objects.get(id=pet_id)
    context = {
        "pet_detail":pet
    }
    return render(request, 'home/beforeLogin.html', context)

def logout_user(request):
    logout(request)
    return redirect('/')


@user_only
def describe_before_login(request):
    return render (request, 'home/beforeLogin.html')




@unauthenticate_user
def signup(request):
    form = CreateUserForm()
     
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account was created successfully')
            return redirect('login')
        else:
            messages.error(request, "error")

 
    context = {'form':form}
    return render(request, 'home/signup.html',context)



@unauthenticate_user
def login_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {'form':form}    
    return render(request, 'home/login.html', context)



@unauthenticate_user
def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('newpassword')
        password2 = request.POST.get('confirmpassword')

        if (password1 == password2):
    
            user = User.objects.create_user(first_name = firstname,
                                            last_name = lastname,
                                            username = username,
                                            email = email,
                                            password = password1)
            if user:
                messages.success(request, "User is created succesfully")


        
        else:
            messages.error(request,"ERROR IN ENTRY FIELDS")

        return redirect('/login')




