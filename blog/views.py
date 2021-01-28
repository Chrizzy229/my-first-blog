from django.shortcuts import render
from django.utils import timezone
# include the model we have written in models.py
# The dot before models means current directory or current application. 
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})