from django.shortcuts import render,redirect
from .forms import PropertyForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login/')
def Property_register_view(request):
    form = PropertyForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        user = request.user.username
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/account/dashboard')

    return render(request,'dashboard/registerpro.html',{'form':form})

