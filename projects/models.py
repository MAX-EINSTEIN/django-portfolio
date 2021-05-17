from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(default='Hello, World!', max_length=50)
    description = models.TextField(default='Welcome to the world of programming!') 