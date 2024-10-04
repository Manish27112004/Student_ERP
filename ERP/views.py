from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F                        #for OR operations
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from StudentManagement.models import Student


def say_truth(request):
    profile_set = Student.objects.all()
    return render(request, 'hello.html', {'students': profile_set})  # Pass the data as 'students'


def todo(request):
    return render(request, 'todo.html')



