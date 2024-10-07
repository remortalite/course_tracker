from django.urls import path

from .views import TaskCreateView, TaskListView, TaskDetailView


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks.home'),
    path('create/', TaskCreateView.as_view(), name='tasks.create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='tasks.detail'),
]
