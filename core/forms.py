from django import forms

class ContactForm(forms.Form):
        name = forms.CharField(label="",
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),
                                required=True)
        email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
                                 required=True)
        subject = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
                                  max_length=100,
                                  required=True)
        message = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Message'}),
                                    required=True)
