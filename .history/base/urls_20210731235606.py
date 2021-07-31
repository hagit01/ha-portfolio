from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path('', views.home, name="home"),
    path('project/<str:pk>/', views.projectPage, name="project"),
    path('add-project/', views.addProject, name="add-project"),
    path('edit-project/<str:pk>/', views.editProject, name="edit-project"),
    path('inbox/', views.inboxPage, name="inbox"),
    path('inbox/<str:pk>/', views.messagePage, name="message"),
        path('add-project/', views.addProject, name="add-project"),


]
