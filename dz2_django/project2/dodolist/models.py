from django.db import models

# Create your models here.

class dodolist(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='dodolist/images/', blank=True)