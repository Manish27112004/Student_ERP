from django import forms
from .models import Task,Group, Student

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['taskName', 'completed']
        widgets = {
            'taskName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Name'}),
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['groupName', 'students']  # Allow selecting group name and students

    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), widget=forms.CheckboxSelectMultiple)  # List all students with checkboxes
