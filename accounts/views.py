from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import UserLoginForm ,UserForm,ProfileForm
from .models import UserProfile
from promanage.models import Property,Notification


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

def home(request):
    if request.user.is_authenticated:
        return redirect('/account/dashboard')
    else:
        return redirect('/account/login')


@login_required(login_url='/account/login/')
def dashboard(request):
    pro_count = Property.objects.filter(user=request.user).count()
    context = {
        'user':request.user,
        'pro_count':pro_count
    }
    return render(request,'dashboard/dashboard.html',context)

@login_required(login_url='/account/login/')
def all_notifications(request):
    notifications = Notification.objects.filter(to_user =request.user)
    unread_notifications = Notification.objects.filter(to_user=request.user,is_read=False)
    count = len(unread_notifications)
    context={
        'notifications': notifications,
        'count': count,
        'user':request.user
    }
    return render(request,'dashboard/notifications.html',context)

@login_required(login_url='/account/login/')
def newsupdates(request):
    return render(request,'dashboard/news&updates.html',{})

@login_required(login_url='/account/login/')
def billing(request):
    return render(request,'dashboard/billing.html',{})

@login_required(login_url='/account/login/')
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=request.user)
        profle_form = ProfileForm(request.POST,instance=request.user.userprofile)
        if user_form.is_valid() and profle_form.is_valid():
            user_form.save()
            profle_form.save()
            print("updated")
            #return redirect()
        else:
            print("not updated")
    else:
        user_form = UserForm(instance=request.user)
        profle_form = ProfileForm(instance=request.user.userprofile)
    return render(request,'dashboard/profile.html',{
        'user':request.user,
        'user_form':user_form,
        'profile_form':profle_form
    })
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        form.new_password1.help_text=''
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('accounts:change_password')
    else:
        form = PasswordChangeForm(request.user)
    context ={
        'form':form,
        'user':request.user,
    }
    return render(request,'dashboard/change_password.html',context)
