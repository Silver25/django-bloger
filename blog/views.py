from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
# Post (with a capital P) always refers to the 'Post' model in model.py created. 
# On the other hand, 'post' (with a lowercase p) refers to an individual blog post
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    # template_name = "post_list.html"  DELETE <-
    template_name = "blog/index.html"
    paginate_by = 6  # number of post titles/excerpts to be displayed on page

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    # pull only Published posts from db - models.py-STATUS=1
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)  # get data or raise a Http404 error

    return render(
        request,
        "blog/post_detail.html",  # path to the template file
        {"post": post},  # set the name of the object
    )   # context is how we pass data from our views to our templates
    # context is a Python dictionary of key/value pairs that is sent to the template
    # It is convention that the key name would be the same as the variable name