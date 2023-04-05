from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse as render
# from django.http import HttpResponse
from .models import *
from .middleware import my_middleware
# Create your views here.


def index (request):
    # print(request.headers)
    sign= signup.objects.all()
    context={
        'sign': sign
    }
    return render(request, 'home.html', context)
    
def template(request):
    context={
        "Meta": request.META
    
    }
    context={
        "Headers": request.headers
    
    }
    context={
        "Method": request.method

    }
    
    return render(request, 'user.html', context)