from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Property,Notification
from .forms import PropertyForm,MaintenanceRequestForm,ToLetForm

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

@login_required(login_url='/account/login/')
def property_detail(request,id=None):
    instance = get_object_or_404(Property,id=id)
    context={
        'instance':instance
    }
    return render(request,'dashboard/property_detail.html',context)
@login_required(login_url='/account/login/')
def maintenace_request(request,id=None):
    property_instance = get_object_or_404(Property,id = id)
    form = MaintenanceRequestForm(request.POST or None)
    if form.is_valid():
        form_instance = form.save(commit=False)
        form_instance.user =request.user
        form_instance.property = property_instance
        form_instance.save()
        messages.success(request, "Maintenance Request Successful")
        return redirect('/account/dashboard/manage_property/properties/')
    context={
        'form':form
    }
    return render(request,'dashboard/maintenance_request.html',context)
@login_required(login_url='/account/login/')
def to_let_view(request,id = None):
    property_instance = get_object_or_404(Property,id = id)
    form = ToLetForm(request.POST or None , instance=property_instance)
    if form.is_valid():
        form_instance = form.save(commit=False)
        form_instance.user = request.user
        form_instance.property = property_instance
        form_instance.save()
        return redirect('/account/dashboard/manage_property/properties/')
    context = {
        'form':form
    }
    return render(request,"dashboard/tolet.html",context)