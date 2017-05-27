from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render,redirect
from .forms import UserLoginForm


def home(request):
    return redirect('/account/login')

def login_view(request):
    print(request.user.is_authenticated())
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        print(request.user.is_authenticated())
        #redirect('/account/dashboard')
    return render(request,'accounts/login.html',{"form":form})

def logout_view(request):
    logout(request)
    return redirect('/account/login')
