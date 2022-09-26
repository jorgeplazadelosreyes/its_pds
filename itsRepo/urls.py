from django.urls import path
from . import views

urlpatterns = [
    path("home_admin", views.CreateHomework.as_view(), name="home_admin"),
    path("", views.LoginPage.as_view(), name= "login"),
    path("register", views.RegisterPage.as_view(), name= "register"),
    path("homework/<homework_id>/edit_diagram", views.EditDiagram.as_view(), name="edit_diagram"),
    path("homework/<homework_id>/", views.ViewHomework.as_view(), name="save_homework"),
    path("statement/<homework_id>/", views.SaveFile.as_view(), name="save_statement_file"),
    path("homework/<homework_id>/edit_forces", views.EditForces.as_view(), name="edit_forces"), 
    path("homework/<homework_id>/diagram_forces", views.DiagramForces.as_view(), name="diagram_forces"),
    path("homework/<homework_id>/balance_equations", views.BalanceEquations.as_view(), name="balance_equations"),
    path("students", views.ViewStudents.as_view(), name = "view_students"),
    path("student", views.StudentHome.as_view(), name = "student_home"),
    path("do_homework/<homework_id>", views.NextHomework.as_view(), name = "next_homework"),
    path("logout", views.LogoutUser.as_view(), name = "logout"),
    path("homework/<homework_id>/delete", views.DeleteHomework.as_view(), name = "delete_homework")
] 