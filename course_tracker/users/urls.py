from django.urls import path

from .views import CreateUserView, UpdateUserView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='users.create'),
    path('<int:pk>/update/', UpdateUserView.as_view(), name='users.update'),
]
