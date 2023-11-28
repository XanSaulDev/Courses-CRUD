from django import forms
from courses.models import User, Course

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['categories'].widget.attrs.update({'class': 'form-control'})
        self.fields['instructor'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['instructor'].queryset = User.objects.filter(role=User.RoleChoices.INSTRUCTOR)
