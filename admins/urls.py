from . import views
from django.urls import path
from django.http import HttpResponse


urlpatterns = [ 
    path('admin',views.admins),
    path('useradmin',views.user_display),
    path('changetouser/<str:username>',views.admin_change_user),
    path('changetoadmin/<str:username>',views.user_change_admin),
    path('deleteuser/<int:user_id>',views.delete_user),
    path('deletestory/<int:story_id>',views.deletestory),
    path('story',views.viewstory),
    path('deleteadopt/<int:adopt_id>',views.deleteadopt),
    path('viewadapt',views.viewadopt)

    # path('deletepost',views.user),
    # path('deletestories',views.use),
]
