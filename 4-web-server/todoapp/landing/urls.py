from django.urls import path
from .views import index

urlpatterns = [
  # path(path to visit, function to run when path is loaded,  name to reference a path)
  path('', index, name='index')
]