
from django.contrib import admin
from .models import teacher, faculty, course

class teacherAdmin(admin.ModelAdmin):
 list_display = ('last_name', 'first_name', 'date_of_birth')
admin.site.register(teacher, teacherAdmin)


class courseAdmin(admin.ModelAdmin):
        pass
admin.site.register(course, courseAdmin)
admin.site.register(faculty)

# Register your models here.
