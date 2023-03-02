from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import DashboardView
from essivi.views import RegisterUserView

urlpatterns = [
    # /essivi/login
    path('login/', view=LoginView.as_view(template_name="essivi/login.html"), name="login"),
    path('logout/', view=LogoutView.as_view(), name='logout'),
    path('dashboard/', view=DashboardView.as_view(), name="dashboard"),
    path('register/', view=RegisterUserView.as_view(), name='register'),
]