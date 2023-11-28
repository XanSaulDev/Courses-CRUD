from django.shortcuts import render
from .models import Course
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from .forms.Course import CourseForm

def index(request):

    courses= Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'index.html', context)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('course-list')

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_update.html'
    form_class = CourseForm
    success_url = reverse_lazy('course-list')


class CourseCreateView(CreateView):
    model = Course
    template_name = 'course_create.html'
    success_url = reverse_lazy('course-list')
    form_class = CourseForm


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'