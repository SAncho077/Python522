from django.shortcuts import render

from dodolist.models import dodolist


# Create your views here.


def index(request):
    projects = dodolist.objects.all()
    return(render(request, 'dodolist/index.html', {'projects': projects}))