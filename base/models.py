from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    staus = models.CharField(max_length=200)