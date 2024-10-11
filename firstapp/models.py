from django.db import models
from django.urls import reverse

class faculty(models.Model):
    name = models.CharField(max_length=200, help_text="Введите наименование факультета")
    def _str_(self):
        return self.name

class course(models.Model):
    title = models.CharField(max_length=200, help_text="")
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Введите описание учебного курса")
    faculty = models.ManyToManyField(faculty, help_text="Введите факультет")
    def _str_(self):
        return self.title
    def get_absolute_url(self):
        return reverse('Данные о курсе', args=[str(self.id)])

class teacher(models.Model):
    first_name = models.CharField(max_length=100, help_text="")
    last_name = models.CharField(max_length=100, help_text="")
    date_of_birth = models.DateField(null=True, blank=True)
    def get_absolute_url(self):
        return reverse('Данные о преподавателе', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)





























