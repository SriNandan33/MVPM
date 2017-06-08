from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile
User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField(label="",
                                widget = forms.TextInput(attrs={'class': 'form-username form-control', 'placeholder': 'Username'}),
                               )
    password = forms.CharField(label="",
                                widget = forms.PasswordInput(attrs={'class': 'form-password form-control', 'placeholder': 'Password'}),
                               )
    def clean(self, *args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("User does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user no longer active.")
            return super(UserLoginForm,self).clean(*args,**kwargs)

#updateprofileform = UserForm + ProfileForm
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude= ('user',)
