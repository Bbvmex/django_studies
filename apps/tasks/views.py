from django.shortcuts import get_object_or_404, render, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(title=title, description=description)
        return redirect("task_list")
    return render(request, "tasks/add_task.html")


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.toggle_completed()
    return redirect("task_list")
