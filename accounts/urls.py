from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LogInForm


app_name= 'accounts'


urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.SignUp,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=LogInForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('terms&conditions/',views.terms,name='terms'),
]