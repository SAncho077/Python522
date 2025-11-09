from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate



from django.contrib.auth.decorators import login_required


from .models import Course


@login_required
def pricing(request):
    course = Course.objects.all()
    return render(request, "course/pricing.html", {'course': course})

@login_required
def detail(request, cour_id):
    cour = get_object_or_404(Course, pk=cour_id)
    return render(request, 'course/details.html', {'cour': cour})


def signup_user(request):
    if request.method == "GET":
        return render(request, 'course/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('pricing')
            except IntegrityError:
                return render(request, 'cource/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def login_user(request):
    if request.method == "GET":
        return render(request, 'course/loginuser.html', {'form': AuthenticationForm()})

    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'course/loginuser.html', {'form': AuthenticationForm(), 'error': "Неверные данные для входа"})
        else:
            login(request, user)
            return redirect('pricing')