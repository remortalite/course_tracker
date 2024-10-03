from django.urls import path

from . import views


urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses.home'),
    path('create/', views.CourseCreateView.as_view(), name='courses.create'),
    path('<int:pk>/update/', views.CourseUpdateView.as_view(),
         name='courses.update'),
    path('<int:pk>/', views.CourseDetailView.as_view(),
         name='courses.detail'),
    path('<int:pk>/delete', views.CourseDeleteView.as_view(),
         name='courses.delete'),
]
