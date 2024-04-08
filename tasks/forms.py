from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                'class': 'form-control',
            }
            self.fields[str(field)].widget.attrs.update(new_data)

    class Meta:
        model = Task
        fields = ('title', 'description', 'done')
