from django.shortcuts import render
from django.http import HttpResponse

#def say_truth(request):
     #return HttpResponse("I am Death Nigga")

def say_truth(request):
    return render(request, 'hello.html')