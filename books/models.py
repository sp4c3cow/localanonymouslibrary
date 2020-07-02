from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='books_cover/', default='cover-not-exists.png')
    files = models.FileField(upload_to='documents/', max_length=500)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    body = models.TextField(max_length=1500)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.username)