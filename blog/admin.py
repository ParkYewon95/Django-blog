from django.contrib import admin
from .models import Post
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Post)
#site.register(Post)
