from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.say_hello),
    path("grid/", views.grids, name="etapa 1"),
    path("gr/", views.gr),
    path("etapa2/", views.etapa2, name="etapa 2"),
    path("etapa3/", views.etapa3, name="etapa 3"),
    path("etapa4/", views.etapa4, name="etapa 4")
] 