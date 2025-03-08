from django.urls import path
from todo import views

urlpatterns = [
    path('api/v1/tasks/', views.TaskListView.as_view()),
    path('api/v1/task/<int:pk>/', views.TaskDetailView.as_view()),
    
]