from .import views
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.main, name = 'home'),
    path('login',views.login_user ,name="login"),
    path('signup',views.signup, name="signup"),
    path('shop', views.shop, name = "shop"),
    path('about', views.about, name = 'about'),
    path('adopt',views.adapt, name = 'adapt'),
    path('adopt/<int:pet_id>',views.pet_details, name = 'pet_details'),
    path('register',views.register),
    path('logout',views.logout_user),
    path('describe',views.describe_before_login),
    path('userPet',views.pet),
   
    path('story',views.story),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="home/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="home/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset_change.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="home/password_reset_done.html"),
         name="password_reset_complete"),
]
