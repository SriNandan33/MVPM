from django.shortcuts import render,redirect
from .forms import PropertyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Property,Notification

@login_required(login_url='/account/login/')
def Property_register_view(request):
    form = PropertyForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        user = request.user.username
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,"Property Registered successfully")
        return redirect('/account/dashboard/manage_property/properties/')
    return render(request,'dashboard/registerpro.html',{'form':form})

@login_required(login_url='/account/login/')
def propertylist(request):
    properties = Property.objects.filter(user=request.user).order_by('-date')
    return render(request,'dashboard/property_list.html',{'properties':properties})
