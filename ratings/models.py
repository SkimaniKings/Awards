from django.db import models
from django.contrib.auth.models import User
import datetime as dt



# Create your models here.

class Profile(models.Model):
      
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="roman_reigns.jpg")
    contact = models.CharField(max_length=80 ,null=True)
    
    
    def __str__(self):
            return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    
class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=250)
    

    
    def __str__(self):
        return self.title
    

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

  