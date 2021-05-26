from django.contrib.auth import decorators
from django.http import HttpResponse
from django.shortcuts import redirect

# restrict logged in user
def unathenticated_user(view_func):
    def wrapper_func(response, *args, **kwargs):
        if response.user.is_authenticated :
            return redirect('/dashboard')
        else :
            return view_func(response, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(response, *args, **kwargs):

            group = None
            if response.user.groups.exists():
                group = response.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(response, *args, **kwargs )
            else :
                return HttpResponse('You are not authorized to view this page')

        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(response, *args, **kwargs):

        group = None
        if response.user.groups.exists():
            group = response.user.groups.all()[0].name

        if group == "Admin":
            return view_func(response, *args, **kwargs )
        else :
            return redirect('/profile')

    return wrapper_func

