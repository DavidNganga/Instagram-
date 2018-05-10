from .models import Image
from django import forms
class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude=[]
