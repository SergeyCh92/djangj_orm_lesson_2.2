from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.all()
    object_list2 = Teacher.objects.all()
    context = {'object_list': object_list, 'object_list2': object_list2}

    return render(request, template, context)
