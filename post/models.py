from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="")
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    video = models.FileField(upload_to='video', null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.user ) + self.title

    class Meta:
        db_table = 'Post'
        indexes = [
            models.Index(fields=['user']),
        ]
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class Comment(models.Model):
    post = models.ForeignKey('Post',related_name='comment', on_delete=models.CASCADE)
    by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.by)} commented as {str(self.comment)} in {str(self.post)}"

    class Meta:
        db_table = 'comment'
        ordering = ['-date']
        indexes = [
            models.Index(fields=['by'])
        ]
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class Like(models.Model):
    post = models.ForeignKey('Post', related_name='like', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey('Comment', related_name='like', on_delete=models.CASCADE,null=True, blank=True)
    by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='like', on_delete=models.CASCADE)
    like = models.IntegerField(default=1
    )

    def __str__(self):
        return f"{str(self.by)} hits like in {str(self.post)}"

    class Meta:
        db_table = 'like'