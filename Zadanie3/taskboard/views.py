from django.http import JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt
import json

def task_list(request):
    if request.method == "GET":
        tasks = list(Task.objects.values())
        return JsonResponse(tasks, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        task = Task.objects.create(title=data["title"])
        return JsonResponse({"id": task.id, "title": task.title, "completed": task.completed})

@csrf_exempt
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "PATCH":
        data = json.loads(request.body)
        task.completed = data.get("completed", task.completed)
        task.save()
        return JsonResponse({"id": task.id, "title": task.title, "completed": task.completed})
    elif request.method == "DELETE":
        task.delete()
        return JsonResponse({"deleted": True})
