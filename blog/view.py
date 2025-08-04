from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})



# return render(request, 'blog/home.html', {'posts': posts}) 
# The same request from post_list(request) goes here in return and as the home is inside blog we write in this way 