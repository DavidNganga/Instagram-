from .forms import PostForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Profile,Image
# Create your views here.
@login_required(login_url='/accounts/login')
def welcome(request):
    profiles = Profile.get_all()
    images = Image.get_all()
    return render(request, 'welcome.html', {"images":images}, {"profile":profiles})

def photo_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            Profile.user = current_user
            image.save()
            return redirect('welcome')
    else:
        form = PostForm()
    return render(request, 'post.html', {"form": form})

def all(request):
    return render(request,"welcome.html")

def prof(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            Profile.user = current_user
            profile.save()
            return redirect('viewprofile')
    else:
            form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

def viewprofile(request):
    pics = Profile.get_all()
    return render(request, 'viewprofile.html', {"pics":pics})


def search_results(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        print(search_term)

        profiles = Profile.search_results(search_term)
        message = f"{search_term}"
        

        return render(request, 'search.html',{"message":message,"profiles": profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
