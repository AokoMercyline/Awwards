from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from datetime import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
filename = '/home/mercy/Documents/Awwards/media/default.jpg'
# Create your tests here.
class TestPostModel(TestCase):
    def setUp(self):
        self.user = User(username="testuser",password="adminpass")
        self.user.save()
        # filename = '/home/moringa/Desktop/Awwards/media/default.jpg'
        self.post = Post(
            image= SimpleUploadedFile(name='test_image.jpg', content=open(filename, 'rb').read(), content_type='image/jpeg'),
            title="post title",
            desc="post desc",
            link="http://test.link.com",
            user=self.user,
            post_date=datetime.now(),
            technologies='lorem, ipsum, dolor, sit, amet'
        )
    def test_post_create(self):
        self.post.save()
        query = Post.objects.all()
        self.assertTrue(len(query)>0)
        
    def test_post_update(self):
        self.post.save()
        test_title = 'updated_title'
        self.post.title = test_title
        self.post.save()
        self.assertTrue(self.post.title,test_title)
        
    def test_delete_post(self):
        self.post.save()
        self.post.delete()
        query =Post.objects.all()
        self.assertIs(len(query),0)
        
    def test_post_is_instance(self):
        self.post.save()
        query = Post.objects.all()
        self.assertIsInstance(query[0],Post)
        
# class TestUsernameModel(TestCase):
#     def setUp(self):
#         self.title ='test title'
#         self.desc ="Lorem ipsum dolor sit amet"
#         self.image= SimpleUploadedFile(name='test_image.jpg', content=open(filename, 'rb').read(), content_type='image/jpeg')
    
#     def test_username_create(self):
#         self.username.save_username()
#         query = Username.objects.all()
#         self.assertTrue(len(query)>0)
        
#     def test_username_update(self):
#         self.username.save_username()
#         test_desc = 'updated desc'
#         self.username.desc = test_desc
#         self.username.update_username()
#         self.assertTrue(self.username.desc,test_desc)
        
#     def test_delete_username(self):
#         self.username.save_username()
#         self.username.delete_username()
#         query =Username.objects.all()
#         self.assertIs(len(query),0)
        
#     def test_username_is_instance(self):
#         self.username.save()
#         query = Username.objects.all()
#         self.assertIsInstance(query[0],Username)