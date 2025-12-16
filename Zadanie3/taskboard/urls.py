from django.urls import path
from taskboard import views

urlpatterns = [
    path('', views.task_list, name='task-list'),  # teraz /tasks/ wywoła task_list
    path('api/tasks/', views.task_list, name='task-list-api'),
    path('api/tasks/<int:task_id>/', views.task_detail, name='task-detail-api'),
]
