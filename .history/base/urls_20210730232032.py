from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<str:pk>/', views.projectPage, name="project"),
    path('add-project/', views.addProject, name="add-project")
]
