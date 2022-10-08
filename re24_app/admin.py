from django.contrib import admin
from re24_app.models import *

# Register your models here.
class studentmark(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'mrk', 'sub',)
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.modified_by = request.user
        instance.save()
        form.save_m2m()
        return instance
admin.site.register(Mark, studentmark)   


class student_id(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Age', 'City','DOB')    
admin.site.register(Student, student_id)
