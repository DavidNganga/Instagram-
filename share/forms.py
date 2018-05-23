from .models import Image,Profile,Comment
from django import forms
'''
a form for posting new images,captions
'''
class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude=["profile" "user"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=["user"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude=["author","image"]
