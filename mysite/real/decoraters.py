from pickle import NONE
from django.http import HttpResponse
from django.shortcuts import redirect,render

def unautheticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorater(view_func):
        def wrapper_func(request,*args,**kargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kargs)
            else:
                return HttpResponse('not allowed')
        return wrapper_func
    return decorater

def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        print(request.user.groups.all())
        if group == 'admin':
            return view_func(request,*args,**kwargs)
        return render(request,'home1/home.html')
    return wrapper_func