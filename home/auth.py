
from django.http import HttpResponse
from django.shortcuts import redirect



def unauthenticate_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('/admins/admin')
            elif not request.user.is_staff:
                return redirect('/')
            return redirect('/')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function

def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return view_function(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_function

    
def user_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('/admins/admin')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper_function