from . import views
from django.urls import path
from django.http import HttpResponse


urlpatterns = [
    path('myadmin',views.admin ,name="login"),

]
