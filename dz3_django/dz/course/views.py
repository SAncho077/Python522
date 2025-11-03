from django.shortcuts import render, get_object_or_404
from .models import Course

def pricing(request):
    course = Course.objects.all()
    return render(request, "course/pricing.html", {'course': course})

def detail(request, cour_id):
    cour = get_object_or_404(Course, pk=cour_id)
    return render(request, 'course/details.html', {'cour': cour})

# Create your views here.
