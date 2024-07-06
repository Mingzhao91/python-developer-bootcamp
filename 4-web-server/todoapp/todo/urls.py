from django.urls import path
from .views import index, AboutView, task

urlpatterns = [
  # path(path to visit, function to run when path is loaded,  name to reference a path)
  path('', index, name='index'),
  path('about/', AboutView.as_view(), name='about'),
  path('task/<int:id>', task, name='task')
]