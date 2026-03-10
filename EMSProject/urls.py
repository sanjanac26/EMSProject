"""
URL configuration for EMSProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from emsapp import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('employees/', views.EmployeeListView.as_view(), name="display"),
    path('employees/add/', views.EmployeeCreateView.as_view(), name="insert"),
    path('employees/<int:e_id>/edit/', views.EmployeeUpdateView.as_view(), name="edit"),
    path('employees/<int:e_id>/delete/', views.EmployeeDeleteView.as_view(), name="delete"),
    path('search/', views.EmployeeListView.as_view(template_name="emsapp/search.html"), name="search"),
    # authentication
    path('login/', auth_views.LoginView.as_view(template_name='emsapp/login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

