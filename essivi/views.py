from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from essivi.forms import RegisterUserForm
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseForbidden
from .models import Product
from .forms import ProductForm
from .models import Category
from .forms import CategoryForm
from .models import Brand
from .forms import BrandForm
from .models import Custommer
from .forms import CustommerForm
from django.contrib.auth import get_user_model






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
    


###################################################################################################
#
#                                  PRODUCT
#
###################################################################################################

@login_required(login_url='/essivi/login/')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products}) 

@login_required(login_url='/essivi/login/')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

@login_required(login_url='/essivi/login/')
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

@login_required(login_url='/essivi/login/')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

###################################################################################################
#
#                                  CATEGORY
#
###################################################################################################

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories}) 


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})

###################################################################################################
#
#                                  BRAND
#
###################################################################################################

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brand_list.html', {'brands': brands}) 


def brand_create(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand_list')
    else:
        form = BrandForm()
    return render(request, 'brand_form.html', {'form': form})

def brand_update(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand_list')
    else:
        form = BrandForm(instance=brand)
    return render(request, 'brand_form.html', {'form': form})

def brand_delete(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        brand.delete()
        return redirect('brand_list')
    return render(request, 'brand_confirm_delete.html', {'brand': brand})


###################################################################################################
#
#                                  CUSTOMMER
#
###################################################################################################

def custommer_list(request):
    custommers = Custommer.objects.all()
    return render(request, 'custommer_list.html', {'custommers': custommers}) 


def custommer_create(request):
    if request.method == 'POST':
        form = CustommerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('custommer_list')
    else:
        form = CustommerForm()
    return render(request, 'custommer_form.html', {'form': form})

def custommer_update(request, pk):
    custommer = get_object_or_404(Custommer, pk=pk)
    if request.method == 'POST':
        form = CustommerForm(request.POST, instance=custommer)
        if form.is_valid():
            form.save()
            return redirect('custommer_list')
    else:
        form = CustommerForm(instance=custommer)
    return render(request, 'custommer_form.html', {'form': form})

def custommer_delete(request, pk):
    custommer = get_object_or_404(Custommer, pk=pk)
    if request.method == 'POST':
        custommer.delete()
        return redirect('custommer_list')
    return render(request, 'custommer_confirm_delete.html', {'custommer': custommer})
