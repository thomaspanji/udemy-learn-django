from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("Hello World")

def february(request):
    return HttpResponse("This is February")
