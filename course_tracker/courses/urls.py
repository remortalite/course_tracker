from django.urls import path

from .views import CoursesListView, CourseCreateView


urlpatterns = [
    path('', CoursesListView.as_view(), name='courses.home'),
    path('create/', CourseCreateView.as_view(), name='courses.create'),
]
