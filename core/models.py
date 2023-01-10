from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
import uuid
from datetime import datetime
from django import forms
from django.core.validators import FileExtensionValidator

User = get_user_model()

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(null=True)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to='profile_images', default='blank-person-icon.jpg')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    num_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    file = models.FileField(null=True,
                            blank=True,
                            validators=[FileExtensionValidator(['pdf'])])
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=500)

    def __str__(self):
        return self.username


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user




class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ManyToManyField(Profile)
    title = models.CharField(max_length=200)
    description = models.TextField()
    starts_at = models.DateTimeField(default=datetime.now)
    ends_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
