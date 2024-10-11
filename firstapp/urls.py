from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path(r'^course/$', views.courseListView.as_view(), name='course'),
    path(r'course/(?P<pk>\d+)/$', views.courseDetailView.as_view(), name='данные о курсе')
]