from .models import Todo
from django.forms import ModelForm

class AddNotesForm(ModelForm):
    class Meta:
        model=Todo
        fields=['todo']