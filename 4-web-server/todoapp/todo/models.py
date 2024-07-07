# python manage.py makemigrations
# python manage.py migrate

from django.db import models
from django.contrib.auth.models import User
# from django.db.models import ForeignKey

# Create your models here.

class TaskModel(models.Model):
  # models.ForeignKey(
  #   table that the foreign key is referencing
  #   on_delete=models.CASCADE: all tasks related to this user are deleted if user is deleted
  # )
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField()
  priority = models.IntegerField()