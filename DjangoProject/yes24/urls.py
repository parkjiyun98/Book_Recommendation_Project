"""yes24 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
import webcrawling.views
import index.views
import category.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',webcrawling.views.first, name="first"),
    path('',index.views.index, name='index'),
    path('home/', webcrawling.views.index, name='webcrawling'),
    path('home/search/',webcrawling.views.searchResult, name='searchResult'),
    path('home/search/cosine',webcrawling.views.my_view, name='my_view'),
    path('category/', category.views.index, name='category'),
    path('category/001001001', category.views.one, name='one'),
    path('category/001001011', category.views.two, name='two'),
    path('category/001001025', category.views.three, name='three'),
    path('category/001001004', category.views.four, name='four'),
    path('category/001001014', category.views.five, name='five'),
    path('category/001001022', category.views.six, name='six'),
    path('category/001001046', category.views.seven, name='seven'),
    path('category/001001015', category.views.eight, name='eight'),
    path('category/001001016', category.views.nine, name='nine'),
    path('category/001001047', category.views.ten, name='ten'),
    path('category/001001009', category.views.eleven, name='eleven'),
    path('category/001001010', category.views.twelve, name='twelve'),
    path('category/001001007', category.views.thirteen, name='thirteen'),
    path('category/001001027', category.views.fourteen, name='fourteen'),
    path('category/001001019', category.views.fifteen, name='fifteen'),
    path('category/001001020', category.views.sixteen, name='sixteen'),
    path('category/001001026', category.views.seventeen, name='seventeen'),
    path('category/001001002', category.views.eighteen, name='eighteen'),
    path('category/001001024', category.views.nineteen, name='nineteen'),
    path('category/001001021', category.views.twenty, name='twenty'),
    path('category/001001005', category.views.twentyone, name='twentyone'),
    path('category/001001003', category.views.twentytwo, name='twentytwo'),
    path('category/001001044', category.views.twentythree, name='twentythree'),
    path('category/001001013', category.views.twentyfour, name='twentyfour'),
    #path('webcrawling/', include('webcrawling.urls')),
]
