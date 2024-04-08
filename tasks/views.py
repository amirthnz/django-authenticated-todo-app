from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)

    context = {'tasks': tasks}

    return render(request, 'tasks/index.html', context)


def add_task(request, pk=None):
    task = None
    if pk:
        task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect(reverse_lazy('index'))
    else:
        form = TaskForm(instance=task)

    context = {'form': form}

    return render(request, 'tasks/add_task.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect(reverse_lazy('index'))

