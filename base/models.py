from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
# Create your models here.
class Video(models.Model):
    caption = models.CharField(max_length=100)
    video=models.FileField(upload_to="base/%y")
    def _str_(self):
        return str(self.caption)
    
class Gallery(models.Model):
    title = models.CharField(max_length=70)
    tag = models.CharField(max_length=100 ,default='lions',choices=[('birds', 'birds'), ('wildebeest', 'wildebeest'),('buffalo', 'buffalo'), ('rhinos', 'rhinos'), ('elephants', 'elephants'),('lions', 'lions'), ('leopards', 'leopards'), ('Maasai Mara', 'Maasai Mara')])
    
    image = CloudinaryField()

    def __str__(self):
        return str(self.tag) +" | " +str(self.title)
    


class Destination(models.Model):
    thedestination = models.CharField(max_length=70)
    mini_title = models.CharField(max_length=70)
    title = models.CharField(max_length=70)
    tag = models.CharField(max_length=100 ,default='Maasai Mara')
    paragraph1 = models.TextField(default='Maasai Mara')
    paragraph2 = models.TextField(default='Maasai Mara')
    paragraph3 = models.TextField(default='Maasai Mara')
    paragraph4 = models.TextField(default='Maasai Mara')
    paragraph5 = models.TextField(default='Maasai Mara')
    paragraph6 = models.TextField(default='Maasai Mara')
    image = CloudinaryField()

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length=255)
    snippet_image = models.ImageField(null=True,blank=True,upload_to="images/")
    body1 = RichTextField(blank=True, null= True)
    body2 = RichTextField(blank=True, null= True)
    # body = models.TextField()

    def __str__(self):
        return self.title + " | " + str(self.author)
