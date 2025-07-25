from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter image title'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'title': 'Image Title',
            'image': 'Upload Image',
        }