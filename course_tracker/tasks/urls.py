from django.urls import path

from .views import TaskCreateView, TaskListView


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks.home'),
    path('create/', TaskCreateView.as_view(), name='tasks.create'),
]
