from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateHomework.as_view(), name="create_homework"),
    path("homework/<homework_id>/edit", views.EditHomework.as_view(), name="edit_homework"),
    path("homework/<homework_id>/", views.ViewHomework.as_view(), name="save_homework")
    #path("new_homework", )
    #path("gr/", views.gr),
    #path("etapa2/", views.etapa2, name="etapa 2"),
    #path("etapa3/", views.etapa3, name="etapa 3"),
    #path("etapa4/", views.etapa4, name="etapa 4")
] 