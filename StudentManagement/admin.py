from django.contrib import admin
from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'regNo', 'address', 'year', 'division']

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacherID', 'phoneNo', 'position']

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['groupId', 'groupName' ]
    filter_horizontal = ('students',)  # Use a horizontal filter to select multiple students


@admin.register(models.ToDoList)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['taskID', 'taskName']

     
    
