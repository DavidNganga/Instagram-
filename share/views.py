from .forms import PostForm, ProfileForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Profile,Image,Comment,User
from .email import send_welcome_email
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='/accounts/login')
def welcome(request):
    '''
    functions for the landing page
    '''
    current_user=request.user
    print(current_user)
    Profile.user = current_user
    print(Profile.user)

    photos = Profile.objects.all().filter(user=current_user)
    images = Image.objects.all().filter(user=current_user)


    comments = Comment.objects.all()

    return render(request, 'welcome.html', {"images":images,"photos":photos, "comments":comments})


@login_required
def photo_post(request):
    '''
    form for uploading Images to instagram
    '''
    current_user = request.user.id
    user_instance =User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile__user = current_user
            image.user=user_instance
            image.save()
            return redirect('welcome')
    else:
        form = PostForm()
    return render(request, 'post.html', {"form": form})

'''
function to allow posting of comment for specific Images
'''
def post_comment(request, image_id):
    current_image = Image.objects.get(id=image_id)
    current_user = request.user
    if request.method == 'POST':
        '''
        a form for adding Comments
        '''
        # image=get_object_or_404(Images,id=id)
        if request.method=='POST':
            current_user=request.user
            form = CommentForm(request.POST, request.FILES)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = current_user
                comment.image = current_image
                comment.save()
            return redirect('/')
    else:
            form = CommentForm()
    return render(request, 'comment.html', {"form": form, "current_image":current_image,"id":image_id})


@login_required
def imagedetails(request,image_id):
    image = Image.objects.get(id = image_id)
    comment = Comment.objects.filter(image= image)


    is_liked=False
    if image.likes.filter(id=request.user.id).exists():
        is_liked = True

    return render(request, 'imagedetails.html', {"image":image, "comment":comment, id:image_id,"is_liked":is_liked})


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
            return redirect('welcome')
    else:
            form = ProfileForm()
    return render(request, 'profile.html', {"form": form})


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


@login_required
def viewprofile(request, profile_id):
    '''
    view function for displaying a user's profile page
    '''
    current_user = request.user
    current_user.id=request.user.id
    Profile.user = current_user
    profile1=Profile.objects.get(id=profile_id)
    pics = Profile.objects.filter(id = profile_id)
    snaps = Image.objects.filter(profile =profile1 )
    profile2=Profile.objects.get(id=request.user.id)
    is_follow=False
    if profile2.follow.filter(id=profile_id).exists():
        is_follow=True
    #follows=Profile.objects.get(id=request.user.id)


    return render(request, 'viewprofile.html', {"pics":pics, "snaps":snaps, id:profile_id,"is_follow":is_follow})


def likes(request, image_id):
    image = Image.objects.get(id=image_id)
    is_liked=False
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        is_liked=False
    else:
        image.likes.add(request.user)
        is_liked=True

    print(image)

    return redirect(imagedetails, image_id)

def follow(request,user_id):

    follows=Profile.objects.get(user=request.user)
    user1=User.objects.get(id=user_id)
    print(user1)
    is_follow=False
    if follows.follow.filter(id=user_id).exists():
        follows.follow.remove(user1)
        is_follow=False
    else:
        follows.follow.add(user1)
        is_follow=True

    print(follows)


    return redirect(viewprofile ,user1.id)
