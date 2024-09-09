#Map Our Urls to view Function
#It is a URL Configuration Module
from django.urls import path
from . import views


urlpatterns = [

    path('hello/', views.say_truth)
    # Dont Need 'playground/hello' as already defined in storefronts "urls.py"
]