
# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .models import TaskForm
from rest_framework import viewsets
from .models import TaskSerializer
from rest_framework.decorators import action

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'crud/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'crud/task_form.html', {'form': form})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def suggest_category(self, request, pk=None):
        task = self.get_object()
        suggestion = suggest_task_category(task.description)
        return Response({
            'suggested_category': suggestion
        })