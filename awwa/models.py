from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q

class Post (models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    desc= models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='awwa/')
    link = models.CharField(max_length=70)
    technologies = models.CharField(max_length=100)


    def __str__(self):
        return self.title

    def save_awwa(self):
        self.save()

    def delete_awwa(self):
        self.delete()

        
    @classmethod
    def search(cls,searchterm):
        search = Post.objects.filter(Q(title__icontains=searchterm)|Q(desc=searchterm))
        return search


    def get_absolute_url(self): 
        return reverse('post_detail', args=[str(self.id)])
