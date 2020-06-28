"""haruuback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from customers import views
from django.views.generic import TemplateView
app_name = "customers"

urlpatterns = [
    path('email_change', views.EmailChangeCheckView.as_view(), name='email_change'),
    path('email_change_confirm', views.EmailChangeView.as_view(),
         name='email_change_confirm'),
    path('email_change_complete', TemplateView.as_view(
        template_name='customers/email_change_complete.html'),
        name='email_change_complete'),
    path('top', views.TopView.as_view(), name='top'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
