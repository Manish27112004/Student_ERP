#Map Our Urls to view Function
#It is a URL Configuration Module
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.say_truth, name="home"),
    path('login/', views.user_login, name="login"),
    path('register/', views.register_student, name="sregister"),
    # Dont Need 'playground/hello' as already defined in storefronts "urls.py"

    
      
]