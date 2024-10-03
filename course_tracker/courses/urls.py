from django.urls import path

from .views import CoursesListView, CourseCreateView, CourseUpdateView


urlpatterns = [
    path('', CoursesListView.as_view(), name='courses.home'),
    path('create/', CourseCreateView.as_view(), name='courses.create'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='courses.update'),
]
