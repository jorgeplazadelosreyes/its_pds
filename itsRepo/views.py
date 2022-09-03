from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request, "test.html")

def grids(request):
    return render(request, "grid.html")

def gr(request):
    return render(request, "gr.html")

def etapa2(request):
    return render(request, "etapa2.html")

def etapa3(request):
    return render(request, "etapa3.html")

def etapa4(request):
    return render(request, "etapa4.html")

