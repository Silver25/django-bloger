from django.shortcuts import render, get_object_or_404, reverse
# Generic View for the function to create PostList
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
# Post (with a capital P) always refers to the 'Post' model in model.py created. 
# On the other hand, 'post' (with a lowercase p) refers to an individual blog post
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
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
    # retrieves all the data for a single blog post from the Post model
    post = get_object_or_404(queryset, slug=slug)  # get data or raise a Http404 error
    # retrieves all of the comments for the selected post in descending order
    # related_name from the Comment model
    comments = post.comments.all().order_by("-created_on")
    # variable to store retrieved count of the number of comments
    # filter for approved comments on a post only
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'New comment submitted and awaiting approval!'
            )

    comment_form = CommentForm()

    # helper function
    # context ("post") is how we pass data from our views to our templates
    # context is a Python dictionary of key/value pairs that is sent to the template
    # It is convention that the key name would be the same as the variable name
    return render(
        request,
        "blog/post_detail.html",  # path to the template file
        {
            "post": post,  # set the name of the object
            "comments": comments,
            "comment_count": comment_count,  # set the number of the comments
            "comment_form": comment_form, 
        }
    )

# view returns editor to the post webpage after 
# mofification/edit of the comment is finished
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        # instance=comment, will applied any changes to the existing Comment,
        # instead of creating a new one
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        # robust checks for authorship in views so that unauthorised
        # or mistaken actions can be avoided
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    # robust checks for authorship in views so that unauthorised
    # or mistaken actions can be avoided
    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))