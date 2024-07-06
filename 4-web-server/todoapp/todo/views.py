from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def index(request):
  # return HttpResponse('<h1>Todo</h1>')
  return render(request, 'todo/index.html')

# AboutView is the subclass of view
class AboutView(View):
  def get(self, request):
    return HttpResponse('This is the about page')