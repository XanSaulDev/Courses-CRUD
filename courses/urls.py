from django.urls import path
from .views import index, CourseDeleteView, CourseUpdateView, CourseCreateView

urlpatterns = [
    path('', index, name='course-list'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course-edit'),
    path('course/create/', CourseCreateView.as_view(), name='course-create'),
]