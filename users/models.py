from django.db import models
from  django.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default="Hello there!")
    email = models.CharField(blank = True, max_length = 100)

    def __str__(self):
        return  f'{self.user.username}' 

    def save_profile(self):
        self.save()

