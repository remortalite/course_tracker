from django.urls import path

from .views import (TaskCreateView, TaskListView,
                    TaskDetailView, TaskUpdateView, TaskDeleteView)


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks.home'),
    path('create/', TaskCreateView.as_view(), name='tasks.create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='tasks.detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='tasks.update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='tasks.delete'),
]
