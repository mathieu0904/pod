from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from essivi.forms import RegisterUserForm
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseForbidden


# Create your views here.


class DashboardView(TemplateView):
    template_name = "essivi/dashboard.html"

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "essivi/register.html" 

    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return HttpResponse('User registered')