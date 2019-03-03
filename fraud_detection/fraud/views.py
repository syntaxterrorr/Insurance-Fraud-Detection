from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def claim(request):
    return render(request,'claim.html')

def buy(request):
    return render(request,'buy.html')
