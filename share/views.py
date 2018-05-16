from .forms import PostForm, ProfileForm, CommentForm,NewsLetterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Profile,Image,Comment,NewsLetterRecipients,User
from .email import send_welcome_email
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='/accounts/login')
def welcome(request):
    current_user=request.user.id
    Profile.user = current_user
    photos = Profile.get_all()
    images = Image.objects.all().filter(profile__user=current_user)
    comments = Comment.get_all()
    '''
    subscription form for a newsletter
    '''
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('welcome')
            print(comments)
    else:
        form = NewsLetterForm()
    return render(request, 'welcome.html', {"images":images,"photos":photos,"letterForm":form, "comments":comments})

@login_required
def photo_post(request):
    '''
    form for uploading Images to instagram
    '''
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            Image.profile = current_user
            image.save()
            return redirect('welcome')
    else:
        form = PostForm()
    return render(request, 'post.html', {"form": form})
@login_required
def all(request):
    return render(request,"welcome.html")
@login_required
def prof(request):
    current_user = request.user
    if request.method == 'POST':
        '''
        form to edit profile once a user is registered
        '''
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            Profile.user = current_user
            profile.save()
            return redirect('viewprofile')
    else:
            form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

@login_required
def viewprofile(request):
    '''
    view function for displaying a user's profile page
    '''
    pics = Profile.get_all()
    snaps = Image.get_all()

    print(snaps)
    return render(request, 'viewprofile.html', {"pics":pics, "snaps":snaps})

@login_required
def search_results(request):
    '''
    a function to search for profiles using profile names
    '''

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        print(search_term)

        profiles = Profile.search_results(search_term)
        message = f"{search_term}"


        return render(request, 'search.html',{"message":message,"profiles": profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def post_comment(request,id):
    current_user = request.user
    if request.method == 'POST':
        '''
        a form for adding Comments
        '''
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            Profile.user = current_user
            comment.save()
            return redirect('welcome')
    else:
            form = CommentForm()
    return render(request, 'comment.html', {"form": form, "id":id})

# def userprofile(request,profile_id):
#     profile = Profile.objects.get(id = profile_id)
#     return render(request, 'userprofile.html',{"profile":profile, id: profile_id})
