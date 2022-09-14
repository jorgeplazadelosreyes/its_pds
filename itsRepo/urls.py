from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateHomework.as_view(), name="home_admin"),
    path("homework/<homework_id>/edit_diagram", views.EditDiagram.as_view(), name="edit_diagram"),
    path("homework/<homework_id>/", views.ViewHomework.as_view(), name="save_homework"),
    path("statement/<homework_id>/", views.SaveFile.as_view(), name="save_statement_file"),
    path("homework/<homework_id>/edit_forces", views.EditForces.as_view(), name="edit_forces"),  ##aplicar metodos posts
    path("homework/<homework_id>/diagram_forces", views.DiagramForces.as_view(), name="diagram_forces"),
    path("homework/<homework_id>/balance_equations", views.BalanceEquations.as_view(), name="balance_equations")
] 