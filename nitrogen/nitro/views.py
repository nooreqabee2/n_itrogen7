from django.shortcuts import render
from django.urls import path, include
from .views import *
# Create your views here.

def index(request):
    pass

    return render(request , 'nitro/index.html')