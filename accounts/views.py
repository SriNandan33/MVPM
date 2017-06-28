from django.contrib import messages
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
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UserLoginForm ,UserForm,ProfileForm
from .models import UserProfile
from promanage.models import Property,Notification


def login_view(request):
    next = request.GET.get('next') #incase of login required
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        messages.success(request,"Login Successful")
        if next:
            return redirect(next)
        return redirect('/account/dashboard')
    return render(request,'accounts/login.html',{"form":form})

def logout_view(request):
    logout(request)
    messages.success(request,"Logout Successful.")
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
    unread_notifications = Notification.objects.filter(to_user=request.user, is_read=False)
    read_notifications = Notification.objects.filter(to_user=request.user, is_read=True)
    count = len(unread_notifications)
    context={
        'unread_notifications':unread_notifications,
        'read_notifications': read_notifications,
        'count': count,
        'user':request.user
    }
    return render(request,'dashboard/notifications.html',context)
def mark_all_as_read(request):
   unread_notifications = Notification.objects.filter(to_user=request.user,is_read=False)
   for obj in unread_notifications:
       obj.is_read = True
       obj.save()

   return redirect('/account/dashboard/notifications')
def mark_one_as_read(request,id=None):
      notification = get_object_or_404(Notification,id = id)
      notification.is_read = True
      notification.save()
      return redirect('/account/dashboard/notifications')

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
        profle_form = ProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profle_form.is_valid():
            user_form.save()
            profle_form.save()
            messages.success(request,"Profile Updated Successfully")
        else:
            messages.error(request,"Error Updating Profile")
    else:
        user_form = UserForm(instance=request.user)
        profle_form = ProfileForm(instance=request.user.userprofile)
    return render(request,'dashboard/profile.html',{
        'user':request.user,
        'user_form':user_form,
        'profile_form':profle_form
    })
@login_required(login_url='/account/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Password successfully updated. Please Login again")
            return redirect('/account/login')
        else:
            messages.error(request,"Error Changing the password. Please Try again")
    else:
        form = PasswordChangeForm(request.user)
    context ={
        'form':form,
        'user':request.user,
    }
    return render(request,'dashboard/change_password.html',context)
