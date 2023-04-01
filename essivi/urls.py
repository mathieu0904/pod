from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import DashboardView
from essivi.views import RegisterUserView
from .views import product_list, product_create, product_update, product_delete
from .views import category_list, category_create, category_update, category_delete
from .views import brand_list, brand_create, brand_update, brand_delete
from .views import custommer_list, custommer_create, custommer_update, custommer_delete
#from .views import order_list, order_create, order_update, order_delete

urlpatterns = [
    # /essivi/login
    path('login/', view=LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', view=LogoutView.as_view(), name='logout'),
    path('dashboard/', view=DashboardView.as_view(), name="dashboard"),
    path('register/', view=RegisterUserView.as_view(), name='register'),

    path('product/', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/<int:pk>/update/', product_update, name='product_update'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),

    path('category/', category_list, name='category_list'),
    path('category/create/', category_create, name='category_create'),
    path('category/<int:pk>/update/', category_update, name='category_update'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),

    path('brand/', brand_list, name='brand_list'),
    path('brand/create/', brand_create, name='brand_create'),
    path('brand/<int:pk>/update/', brand_update, name='brand_update'),
    path('brand/<int:pk>/delete/', brand_delete, name='brand_delete'),

    path('custommer/', custommer_list, name='custommer_list'),
    path('custommer/create/', custommer_create, name='custommer_create'),
    path('custommer/<int:pk>/update/', custommer_update, name='custommer_update'),
    path('custommer/<int:pk>/delete/', custommer_delete, name='custommer_delete'),

]