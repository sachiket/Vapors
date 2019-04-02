"""Vapors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from django.contrib.urls import include
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='index.html'), name='home'),
    path('accounts/',include('Vapors_app.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('test/',views.TestPage.as_view(),name='test'),
    path('result/',views.ResultPage.as_view(),name='result'),
    path('case_list/',views.CaseList.as_view(),name='case_list'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),

]
