from django.contrib import admin
from .models import Post

# makes our model visable to the admin page
admin.site.register(Post)