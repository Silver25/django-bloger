from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))  # constant

# Create your models here.
class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)  # must be unique
    slug = models.SlugField(max_length=200, unique=True)  # must be unique
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
)
    # class allows users to upload media to a database model powered by
    # Cloudinary, ensures that image isn't stored in database,
    # but instead sent over to Cloudinary, saving just URL to database
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

#    class Meta:
#        ordering = ["-created_on"]
#
#    def __str__(self):
#        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#        ordering = ["created_on"]
#
#    def __str__(self):
#        return f"Comment {self.body} by {self.author}"
