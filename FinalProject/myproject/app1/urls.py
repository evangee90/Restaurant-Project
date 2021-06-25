"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/',home, name="home"),
    url(r'^register/',register,name="registration"),
    url(r'^login/',login, name="login"),
    url(r'^admins/',adminfunction,name="administrator"),

    url(r'^adminaccess/', adminaccessfunction, name="abc"),
    url(r'^fileuploading/',recipeload, name="recipe"),
    url(r'^totalbill/',adminbilling,name="totalbills"),
    url(r'^adminsgallery/',adminrecipes,name="display"),

    url(r'^mainhome/', mainhome, name="mainhome"),

    url(r'^abouts/',about, name="abouts"),

    url(r'^userdisplay/',userdisplay,name="recipe"),

    url(r'^services/',service, name="services"),

    url(r'^price/(\w+)',quantityselection,name="selectquantity"),

    url(r'^order/',orderbill,name="orderplacing"),
]
