from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateHomework.as_view(), name="create_homework"),
    path("homework/<homework_id>/edit_diagram", views.EditDiagram.as_view(), name="edit_diagram"),
    path("homework/<homework_id>/", views.ViewHomework.as_view(), name="save_homework"),
    path("homework/<homework_id>/edit_forces", views.EditDiagram.as_view(), name="edit_forces")  ##aplicar metodos posts
    #path("etapa3/", views.etapa3, name="etapa 3"),
    #path("etapa4/", views.etapa4, name="etapa 4")
] 