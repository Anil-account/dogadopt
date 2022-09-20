from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.models import *
from home.forms import *
from home.auth import *
import os

@login_required
@user_only
# Create your views here.
def petProfile(request):
    if request.method == "POST":
        data = request.POST
        image = request.FILES.get("image")
        name = data["name"]
        gender = data["gender"]
        age = data["age"]
        breed = data["breed"]
        phone=data["contact"]
        description = data["description"]

        adopt = Adopt(name=name, 
                    image=image, 
                    description=description,
                    age=age,
                    sex=gender,
                    breed=breed,
                    postedby=request.user,
                    contact = phone)
        adopt.save()
        if adopt:
            messages.success(request,"Post has been Uploaded")
        else:
            messages.success(request,"Error in fields data")
        
    return render(request, 'main/petProfile.html')





@login_required
@user_only
def petDesc(request):
    return render(request,'main/petdescription.html')



@login_required
@user_only
def passwordUpdate(request):
    return render(request, 'main/passwordUpdate.html')




@login_required
@user_only
def postStory(request):
        if request.method == "POST":
            data = request.POST
            image = request.FILES.get("image")
            title = data["title"]
            story = data["story"]
            uploadstory = Stories(title=title, 
                        image=image, 
                        details=story,
                        username=request.user
                        )
            uploadstory.save()


            if uploadstory:
                messages.success(request,"Story has been uploaded")
            else:
                messages.success(request,"Entry Filed is Empty")


        #     if uploadstory:
        #        messages.success(request,"succes ")
        #     return redirect('/login')

        return render(request, "main/uploadStory.html")



@login_required
@user_only
def profileUpdate(request):
    user_data = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        
        user = User.objects.filter(username = request.user.username).update(first_name = firstname, last_name = lastname, email = email)


        # profile.save( User.objects.get(username=request.POST['username']))
        
        if user:
            messages.success(request,"Profile has been updated")
        else:
            messages.success(request,"Error in sublitting data")

    else:
        messages.success(request,"Entry Filed is Empty")
        
    context = {
        'user_info':user_data
    }
    

    return render(request, 'main/profileUpdate.html',context)



@login_required
@user_only
def myadopt(request):
    return render(request, 'main/adopteddog.html')



@login_required
@user_only
def userupdatestory(request, story_id):
    story = Stories.objects.get(id=story_id)
    if request.method == "POST":
            data = request.POST
            title = data["title"]
            story = data["story"]

            stry = Stories.objects.filter(id=story_id).update(title=title, details = story)
            
            if stry:
                messages.success(request,"Success")
            else:
                messages.success(request,"Error in sublitting data")

    else:
        messages.success(request,"Entry Filed is Empty")


    context = {
        "story":story
    }
    return  render(request, 'main/userupdatestory.html',context)





@login_required
@user_only
def userupdatepet(request, pet_id):
    pet = Adopt.objects.get(id=pet_id)
    if request.method=="POST":
        data = request.POST
        name = data["name"]
        age = data["age"]
        breed = data["breed"]
        phone=data["contact"]
        description = data["description"]

        user = Adopt.objects.filter(id=pet_id).update(name=name,age=age,breed=breed,contact=phone,description=description)
        if user:
                messages.success(request,"Success")
        else:
            messages.success(request,"Error in submitting data")

    else:
        messages.success(request,"Entry Filed is Empty")



    context = {
        "pet": pet
    }

    return render(request, 'main/userupdatepet.html', context)




@login_required
@user_only
def homeprofile(request):
    pet_detail = Adopt.objects.all().filter(postedby=request.user)
    petstory = Stories.objects.all().filter(username = request.user)
    
    context = {
        "all_pets": pet_detail,
        "story_pet":petstory,
    }

    return render (request, 'main/homeprofile.html',context)




@login_required
@user_only

def userdeletepet(request, pet_id):
    pet = Adopt.objects.get(id=pet_id)
    os.remove(pet.image.path)
    pet.delete()
    return redirect('/user/homeprofile')




@login_required
@user_only
def userdeletestory(request, story_id):
    story = Stories.objects.get(id=story_id)
    os.remove(story.image.path)
    story.delete()
    return redirect('/user/homeprofile')

