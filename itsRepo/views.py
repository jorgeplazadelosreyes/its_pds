from django.shortcuts import render
from django.http import HttpResponse

def grids(request):
    return render(request, "grid.html")

def etapa2(request):
    return render(request, "etapa2.html")

def etapa3(request):
    return render(request, "etapa3.html")

def etapa4(request):
    return render(request, "etapa4.html")

