from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'courses'

urlpatterns = [
    path('all/', CourseListView.as_view(), name='course-all'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('categories/', CourseDetailView.as_view(), name='categories'),
]
