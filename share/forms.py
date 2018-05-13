from .models import Image,Profile,Comment
from django import forms
class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude=[]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=[]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude=[]
