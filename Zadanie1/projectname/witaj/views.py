from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    return HttpResponse("Witaj w Django!")

def hello_name(request, name):
    return HttpResponse(f"Witaj, {name}!")

def hello_template(request, name):
    return render(request, "witaj/hello.html", {"name": name})

def time_view(request):
    current_time = datetime.now()
    context = {
        "date": current_time.strftime("%d-%m-%Y"),
        "time": current_time.strftime("%H:%M:%S"),
    }
    return render(request, "witaj/time.html", context)