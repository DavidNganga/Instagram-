from .models import Image,Profile,Comment,NewsLetterRecipients
from django import forms
'''
a form for posting new images,captions
'''
class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude=["profile","comments", "user"]


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=["user"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude=["author","image"]
