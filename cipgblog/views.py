from django.shortcuts import render
from django.views import generic
from .model import Post


class PostList(generic.PostList):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
    