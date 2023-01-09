from django.contrib import admin
from .models import Post, Profile , LikePost, FollowersCount,File,Event

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
admin.site.register(File)
admin.site.register(Event)