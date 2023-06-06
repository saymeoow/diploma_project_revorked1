from django import forms
from .models import Sneakers, Company, Comments


class AddSneakersForm(forms.ModelForm):
    class Meta:
        model = Sneakers
        fields = ('name', 'slug', 'img', 'description', 'price', 'company', 'available')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {'comment_text'}

        widgets = {
            'name': forms.Textarea(attrs={'class': 'form-control'})
        }
