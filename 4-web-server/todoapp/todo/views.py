from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


tasks = [
  {"id": 1, "name": "Make video", "description":"make vid for course"},
  {"id": 2, "name": "Do dishes", "description":"wash dishes"},
  {"id": 3, "name": "Call mum", "description":"call mum fast"},
]

def get_task_by_id(task_id):
  for task in tasks:
    if task["id"] == task_id:
      return task
    return None

def index(request):
  # return HttpResponse("<h1>Todo</h1>")
  # tasks2 = []
  ctx = {
    "tasks": tasks
  }

  return render(request, "todo/index.html", ctx)

def task(request, id):
  ctx = {
    "task": get_task_by_id(id)
  }
  return render(request, "todo/task.html", ctx)

# AboutView is the subclass of view
class AboutView(View):
  def get(self, request):
    return HttpResponse("This is the about page")