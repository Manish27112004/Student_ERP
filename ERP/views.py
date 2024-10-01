from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F                        #for OR operations
from django.http import HttpResponse
from StudentManagement.models import Student


""" def say_truth(request):
     return HttpResponse("I am Death Nigga") """

def say_truth(request):
    profile_set = Student.objects.all()
    return render(request, 'hello.html')

""" def display_profile(request):
    
    return profile_set """

