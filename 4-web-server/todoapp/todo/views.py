from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import TaskForm
from .models import TaskModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.


tasks = [
  {"id": 1, "name": "Make video", "description":"make vid for course", "priority": 1},
  {"id": 2, "name": "Do dishes", "description":"wash dishes", "priority": 2},
  {"id": 3, "name": "Call mum", "description":"call mum fast", "priority": 3},
]

# def get_task_by_id(task_id):
#   for task in tasks:
#     if task["id"] == task_id:
#       return task
#     return None

# the user must login to be able to run this function, if user hasn't logged in,
# navigate user to todo:login page
@login_required(login_url='todo:login')
def index(request):
  # return HttpResponse("<h1>Todo</h1>")
  # tasks2 = []
  taskform = TaskForm()
  # print('get tasks from sessions')
  # print(request.session['tasks'])

  # get tasks from sessions
  # if not 'tasks' in request.session:
  #   print('no tasks.....')
  #   request.session['tasks'] = []

  # get tasks from table
  tasks = TaskModel.objects.all()

  ctx = {
    "tasks": tasks, #request.session['tasks'],
    "form": taskform,
    "user": request.user
  }

  return render(request, "todo/index.html", ctx)

# go to the 127.0.0.1:8000/admin to access the settings about our application
# to create a super user: python manage.py createsuperuser
# superuser: 
# name: test
# password: 123456
# user:
# name: edwardwhite7
# password: 123456
def login_user(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password) # return None if it's not found
  
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse('todo:index'))
    else:
      return render(request, 'todo/login.html')

  return render(request, 'todo/login.html')

@login_required(login_url='todo:login')
def logout_user(request):
  logout(request)
  return HttpResponseRedirect(reverse('todo:index'))


def task(request, id):
  ctx = {
    # "task": get_task_by_id(id)
    'task': TaskModel.objects.get(id=id)
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
      # {'task': 'fdsafads', 'description': 'fdsafdasfdasfa', 'priority': '1'}
      print(form.cleaned_data)
      # create a task that want to save to session
      # task = {
      #   "id": len(tasks) + 1,
      #   "name": form.cleaned_data['task'],
      #   "description": form.cleaned_data['description'],
      #   "priority": int((form.cleaned_data)['priority'])
      # }
      # request.session['tasks'].append(task)
      # request.session.save()
      # print(request.session['tasks'])

      # create a task and save to db
      task = TaskModel(
        name=form.cleaned_data['task'],
        description=form.cleaned_data['description'],
        priority=int((form.cleaned_data)['priority'])
      )

      # save the task to db
      task.save()

  # the todo is from the urls/app_name = 'todo'
  return HttpResponseRedirect(reverse('todo:index'))



