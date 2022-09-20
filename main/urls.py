from . import views
from django.urls import path
from django.http import HttpResponse

from django.contrib import admin
from django.urls import path
from . import views 
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

def index(request):
    return HttpResponse("This is product page.")


urlpatterns = [
    path('index/',index),
    path('petprofile',views.petProfile),
    path('profileUpdate',views.profileUpdate),
    path('passwordUpdate',views.passwordUpdate),
    path('petdescription',views.petDesc),
    path('uploadStory',views.postStory),
    path('myadoption',views.myadopt),
     path('homeprofile',views.homeprofile),
     path('userupdatepet/<int:pet_id>',views.userupdatepet),
     path('userupdatestory/<int:story_id>',views.userupdatestory),
     path('userdeletepet/<int:pet_id>',views.userdeletepet),
     path('userdeletestory/<int:story_id>',views.userdeletestory),
    path('changepassword', auth_views.PasswordChangeView.as_view(
        template_name='main/changepassword.html')),
    path('passwordchandedone', auth_views.PasswordChangeView.as_view(
        template_name='main/passwordChanged.html'), name='password_change_done'),
]