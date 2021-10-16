from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.utils.translation import activate, deactivate
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.

class Course(models.Model) : 
    name = models.CharField(max_length=200, null=False)
    #description = models.TextField()
    slug= models.CharField(max_length=200, default=name )
    description = RichTextField(blank=True, null= True)
    price = models.IntegerField(null=False)
    discount =models.IntegerField(null=False, default=0)
    active= models.BooleanField(default=False)
    thumbnail=models.ImageField(upload_to="media/images")
    date= models.DateTimeField(auto_now_add=True, null=True)
    slot_1= models.CharField(max_length=200,blank=True, null= True)
    slot_2= models.CharField(max_length=200,blank=True, null= True)
    course_duration =models.CharField(max_length=100,null=False)
    image= models.ImageField (default= 'DEFAULT-IMG.jpg' ,upload_to="media/images")
    Course_avilability= models.BooleanField(default=False)
  
    def __str__(self):
        return self.name

class Tag (models.Model):
    description = models.CharField(max_length=50, null=False)
    Course = models.ForeignKey(Course,null=False, on_delete=models.CASCADE)

class Prerequisit (models.Model):
    description = RichTextField(blank=True, null= True)
    Course = models.ForeignKey(Course,null=False, on_delete=models.CASCADE)

class Resource(models.Model):
    lecture = models.CharField (max_length=200, null=True, blank=True)
    Course = models.ForeignKey(Course,null=False, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files', null=True, blank=True, max_length=500)
    
    def __str__(self):
        
        return self.lecture

class Learning (models.Model):
    description = RichTextField(blank=True, null= True)
    Course = models.ForeignKey(Course,null=False, on_delete=models.CASCADE)


class Teacher(models.Model):
    image = models.ImageField(default= 'avatar.jpeg' ,upload_to="media/images")
    name = models.CharField(max_length=255, null=False)
    phone =models.CharField(max_length=20, null=False)
    email=models.CharField(max_length=200, null=False)
    expert_on = models.CharField(max_length=255,null=False)
    self_intro = RichTextField(blank=True, null= True)
    personal_bio = RichTextField(blank=True, null= True)
    career_histroy = RichTextField(blank=True, null= True)
    educational_qualifications = RichTextField(blank=True, null= True)
    def __str__(self):
        return self.name


class TsdBlog(models.Model):
     image = models.ImageField(default= 'DEFAULT-IMG.jpg' ,upload_to="media/images")
     title =models.CharField(max_length=200, null=True)
     slug= models.CharField(max_length=200, default= title )
     author = models.CharField(max_length=255, null=False)
     date= models.DateTimeField(auto_now_add=True, null=True)
     content = RichTextField(blank=True, null= True)
     def __str__(self):
        return self.title