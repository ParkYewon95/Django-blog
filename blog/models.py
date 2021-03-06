from django.db import models
from django.utils import timezone

class Post(models.Model):
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    #blog 게시글 번호에 해당하는 foreignkey 필드 필요!
    #post = models.ForeignKey('blog.Post', related_name='comments')
    name = models.CharField(max_length=50,blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
