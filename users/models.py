from django.db import models
from  django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.contrib.auth import get_user_model
from django.dispatch import receiver



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default="Hello there!")
    email = models.CharField(blank = True, max_length = 100)

    def __str__(self):
        return  f'{self.user.username}' 

    def save_profile(self):
        self.save()
        
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
