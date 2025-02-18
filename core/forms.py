from django import forms
from core.models import Pen

class PenForm(forms.ModelForm):
    class Meta:
        model = Pen
        fields = ['title', 'description', 'is_public', 'html', 'css', 'js']