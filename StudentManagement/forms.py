from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['taskName', 'completed']
        widgets = {
            'taskName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Name'}),
        }
