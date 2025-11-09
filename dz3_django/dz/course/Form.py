from django.forms import ModelForm
from .models import Course


class TodoForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'descriprion', 'price']