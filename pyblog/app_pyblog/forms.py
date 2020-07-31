from django import forms
from .models import Publicacao

class editorForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['titulo', 'descricao', 'post']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'})
        }