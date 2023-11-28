from django.contrib import admin
from .models import User,Category, Course
from .forms.Course import CourseForm


admin.site.register(Category)
admin.site.register(User)


class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    list_display = ['title', 'instructor', 'price'] 

admin.site.register(Course, CourseAdmin)