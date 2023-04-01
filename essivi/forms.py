from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms 
from .models import Product, Brand
from .models import Category, Custommer


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
    

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['designation', 'price', 'category', 'brand']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['designation']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['designation']

class CustommerForm(forms.ModelForm):
    class Meta:
        model = Custommer
        fields = ['first_name', 'last_name', 'contact', 'address']