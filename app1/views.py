from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    return HttpResponse("<marqueee><h1>index of app2</h1></marquee>")
def sample(request):
    return render(request,"sample1.html")
def sample_app1(request):
    return render(request,'sample_app1.html')

# Create your views here.
