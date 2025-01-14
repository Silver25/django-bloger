from django.shortcuts import render
# from django.http import HttpResponse - remove for templates
from django.views import generic
from .models import Post

# Create your views here.
# def blog(request): - remove for templates
#     return HttpResponse("Hello, Blog!")
class PostList(generic.ListView):
    # model = Post - remove couse redundant by the queryset
    # use only published records from the Post model & display in descending order
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_list.html"