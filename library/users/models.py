from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profiles_pics')
    
    def __str__(self):
        return f'{self.user.username} profile'