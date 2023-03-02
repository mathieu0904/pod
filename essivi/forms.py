from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms 

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']


    def clean_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password']:
            raise ValidationError("Password don't match")
        
        return cd['password']