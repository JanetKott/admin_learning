from django.shortcuts import render
from .models import course, teacher, faculty
from django.views import generic

def index(request):
    num_course = course.objects.all().count()
    num_teacher = teacher.objects.count()
    num_faculty = faculty.objects.count()

    return render(
        request,
        'firstapp/index.html',
       context={'num_course':num_course, 'num_teacher':num_teacher, 'num_faculty':num_faculty},
    )
class courseListView(generic.ListView):
    model = course
class courseDetailView(generic.DetailView):
    model = course
class teacherDetailView(generic.DetailView):
    model = teacher
class teacherListView(generic.ListView):
    model = teacher


