from django import forms
from .models import Movie, Comment

class CreateForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', 'description', 'genre', 'score']
        widgets = {
            'score': forms.NumberInput(attrs={
                'min': 0,
                'max': 5,
                'step': 0.5,
            }),
        }


