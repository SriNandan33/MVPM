from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import ContactForm

def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        message = "Name: " + name + "\n"+"Email: "+ email +"\n"+"Message: "+ message

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

    context ={
            "form":form
        }
    return render(request,"index.html",context)