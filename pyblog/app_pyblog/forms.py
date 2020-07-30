from django import forms
from .models import Publicacao

class editorForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['titulo', 'descricao', 'post']