from django.shortcuts import render
from .models import Task

# Create your views here.
def list_task(request):
    tasks = Task.objects.all()  # Recupera todos los registros de Task
    return render(request, 'list_task.html', {'tasks': tasks})