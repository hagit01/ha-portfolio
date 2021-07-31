from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<pk>/', views.projectPage, name="project")
]
