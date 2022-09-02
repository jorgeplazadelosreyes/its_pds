from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request, "test.html")

def grids(request):
    return render(request, "grid.html")

def gr(request):
    return render(request, "gr.html")