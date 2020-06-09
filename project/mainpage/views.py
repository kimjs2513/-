from django.shortcuts import render
from .models import Post
# Create your views here.

def show_post(request):
    contents = Post.objects.all()
    return render(request, 'posts.html', {'post_list' : contents})

def detail(request, num):
    post = Post.objects.get(id=num)
    return render(request, 'detail.html', {"result" : post})