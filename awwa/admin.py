from django.contrib import admin
from .models import Post
admin.site.site_header='Aoko Developer'


admin.site.register(Post)


