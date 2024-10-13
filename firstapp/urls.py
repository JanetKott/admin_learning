from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('course/', views.courseListView.as_view(), name='course'),
    path('course/<int:pk>/', views.courseDetailView.as_view(), name='course_detail'),
    path('teacher/', views.teacherListView.as_view(), name='teacher'),
    path('teacher/<int:pk>/', views.teacherDetailView.as_view(), name='teacher_detail'),
    ]