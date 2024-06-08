from django.shortcuts import render
from django.views import generic
from .models import Course


class CourseListView(generic.ListView):
    model = Course


class CourseDetailView(generic.DetailView):
    model = Course


def index(request):
    return render(request, 'courses/main.html')
