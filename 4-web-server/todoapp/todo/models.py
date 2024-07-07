# python manage.py makemigrations
# python manage.py migrate

from django.db import models

# Create your models here.

class TaskModel(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  priority = models.IntegerField()