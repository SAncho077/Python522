from django.shortcuts import render
from django.http import HttpResponse
import random

from django.template.defaultfilters import length


# Create your views here.


def home(request):
    lst = list(range(6, 15))
    return render(request, "generator/home.html", {'lst': lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])

    elif request.GET.get("numbers"):
        char.extend([chr(i) for i in range(48, 58)])

    elif request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])

    length = int(request.GET.get('length'))
    psw = ""
    for i in range(length):
        psw += random.choice(char)
    return render(request, "generator/password.html", {'password': psw})


def description(request):
    return(render(request, 'generator/description.html'))
