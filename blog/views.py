from django.shortcuts import render
# from django.http import HttpResponse - remove for templates
from django.views import generic
from .models import Post

# Create your views here.
# def blog(request): - remove for templates
#     return HttpResponse("Hello, Blog!")
class PostList(generic.ListView):
    # model = Post - remove couse redundant by the queryset
    queryset = Post.objects.all()
    template_name = "post_list.html"