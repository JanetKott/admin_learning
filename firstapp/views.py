from django.shortcuts import render
from django.views import generic
from .models import course, teacher, faculty

def index(request):
    num_course = course.objects.all().count()
    num_teacher = teacher.objects.count()

    return render(
        request,
        'firstapp/index.html',
       context={'num_course':num_course, 'num_teacher':num_teacher},
    )
class courseListView(generic.ListView):
    model = course
class courseDetailView(generic.DetailView):
    model = course
