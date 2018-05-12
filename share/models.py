from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    name = models.CharField(max_length=30,null = True)
    bio = models.CharField(max_length = 30)
    profile_photo = models.ImageField(upload_to = 'images/',null = True)
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    # follows=models.ManyToManyField()
    #
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
        name = cls.objects.get(id=id)
        return names


from tinymce.models import HTMLField
class Image(models.Model):
    name = models.CharField(max_length =30)
    caption = models.CharField(max_length = 100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to = 'images/',null = True)
    likes=models.ManyToManyField(User, blank=True, related_name="image_likes")

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

    def get_Image_by_id(cls,id):
        images = cls.objects.get(id=id)
        return images
