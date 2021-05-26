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

