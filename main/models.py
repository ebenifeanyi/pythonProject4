from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    acc= models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    bio = models.TextField()
    pic = models.FileField(upload_to='media', blank=True, null=True)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')

    def __str__(self):
        return self.firstname +' ' + self.lastname

    def get_name(self):
        return self.firstname + ' ' + self.lastname

    def get_friends(self):
        return self.friends.count()

