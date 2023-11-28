from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):

    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name

class User(models.Model):

    class RoleChoices(models.Choices):
        STUDENT = 'student'
        INSTRUCTOR = 'instructor'

    name = models.CharField(max_length=60)
    role = models.CharField(max_length=10, choices=RoleChoices.choices, default=RoleChoices.STUDENT)


    def __str__(self):
        return self.name

class Course(models.Model):

    title  = models.CharField(max_length=60)
    categories = models.ManyToManyField(Category, related_name='categories')
    instructor = models.ForeignKey(User, related_name='instructor', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title