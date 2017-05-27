from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import UserLoginForm


def home(request):
    if request.user.is_authenticated:
        return redirect('/account/dashboard')
    else:
        return redirect('/account/login')

def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next') #incase of login required
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        print(request.user.is_authenticated())
        if next:
            return redirect(next)
        return redirect('/account/dashboard')
    return render(request,'accounts/login.html',{"form":form})

def logout_view(request):
    logout(request)
    return redirect('/account/login')

@login_required(login_url='/account/login/')
def dashboard(request):
    return render(request,'dashboard/dashboard.html',{})

@login_required(login_url='/account/login/')
def newsupdates(request):
    return render(request,'dashboard/news&updates.html',{})

@login_required(login_url='/account/login/')
def billing(request):
    return render(request,'dashboard/billing.html',{})

