from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import TaskForm
# Create your views here.


tasks = [
  {"id": 1, "name": "Make video", "description":"make vid for course", "priority": 1},
  {"id": 2, "name": "Do dishes", "description":"wash dishes", "priority": 2},
  {"id": 3, "name": "Call mum", "description":"call mum fast", "priority": 3},
]

def get_task_by_id(task_id):
  for task in tasks:
    if task["id"] == task_id:
      return task
    return None

def index(request):
  # return HttpResponse("<h1>Todo</h1>")
  # tasks2 = []
  taskform = TaskForm()
  print('get tasks from sessions')
  print(request.session['tasks'])

  if not 'tasks' in request.session:
    print('no tasks.....')
    request.session['tasks'] = []

  ctx = {
    "tasks": request.session['tasks'],
    "form": taskform
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
  

def add_task(request): 
  print(request.POST)

  if(request.method == 'POST'):
    # create a general form inside our python code with data that sent to us prefiill to the form
    form = TaskForm(request.POST)
    if form.is_valid():
      print('is valid')
      # {'task': 'fdsafads', 'description': 'fdsafdasfdasfa', 'priority': '1'}
      print(form.cleaned_data)
      # create a task that want to save
      task = {
        "id": len(tasks) + 1,
        "name": form.cleaned_data['task'],
        "description": form.cleaned_data['description'],
        "priority": int((form.cleaned_data)['priority'])
      }
      request.session['tasks'].append(task)
      request.session.save()
      print(request.session['tasks'])

  # the todo is from the urls/app_name = 'todo'
  return HttpResponseRedirect(reverse('todo:index'))



