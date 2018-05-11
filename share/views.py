from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Profile
# Create your views here.



def welcome(request):
    return render(request, 'welcome.html')



def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            Profile.user = current_user
            image.save()
            print("ggg")
            HttpResponseRedirect('welcome')

    else:
        form = PostForm()
    return render(request, 'post.html', {"form": form})
