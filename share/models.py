from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 30,null = True)
    bio = models.CharField(max_length = 30)
    profile_photo = models.ImageField(upload_to = 'images/',null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    follow=models.ManyToManyField(User,related_name='who_following',blank=True)

    @classmethod
    def get_all(cls):
        pics = cls.objects.all()
        return pics

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def get_Profile_by_id(cls,id):
        names = cls.objects.get(id=id)
        return names

    def get_User_by_id(cls,id):
        usser = cls.objects.get(id=id)
        return usser

    @classmethod
    def search_results(cls,search_term):
         names = cls.objects.filter(name__icontains=search_term)
         return names

    def total_following(self):
        return self.follow.count()

from tinymce.models import HTMLField
class Image(models.Model):
    name = models.CharField(max_length =30)
    caption = models.CharField(max_length = 100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to = 'images/',null = True)
    likes = models.ManyToManyField(User, related_name='image_likes', blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    @classmethod
    def get_all(cls):
        imgs = cls.objects.all()
        return imgs

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    def get_Image_by_id(cls,id):
        images = cls.objects.get(id=id)
        return images

    def get_imagecurrent(cls, current_user):
        images=Image.objects.filter(profile__user=current_user)
        return images

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.CharField(max_length=150, null = True)
    author=models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    image = models.ForeignKey(Image,null = True,on_delete = models.CASCADE)

    def __str__(self):
        return self.post

    def save_comment(self):
        self.save()

    @classmethod
    def get_all(cls):
        opinions = cls.objects.all()
        return opinions

    def get_Comment_by_id(cls,id):
        views = cls.objecs.get(id=id)
        return views
