"""QuizSiteProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from UCDquizApp import views
from django.contrib import admin
from django.conf.urls import include # new
urlpatterns = [
    
    url(r'^$', views.home_page, name='home'),
    url(r'^home.html$', views.home_page, name='home'),
    url(r'^page1.html$', views.page1_page, name='page1'),
    url(r'^page2.html$', views.page2_page, name='page2'),
    url('accounts/', include('django.contrib.auth.urls')),
   # url(r'^$', views.home_page, name='home')
    
]
