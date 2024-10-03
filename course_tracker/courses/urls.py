from django.urls import path

from .views import CourseListView, CourseCreateView, CourseUpdateView, CourseDetailView, CourseDeleteView


urlpatterns = [
    path('', CourseListView.as_view(), name='courses.home'),
    path('create/', CourseCreateView.as_view(), name='courses.create'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='courses.update'),
    path('<int:pk>/', CourseDetailView.as_view(), name='courses.detail'),
    path('<int:pk>/delete', CourseDeleteView.as_view(), name='courses.delete'),
]
