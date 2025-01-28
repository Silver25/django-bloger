from django.shortcuts import render
from .models import About

# Create your views here.
def about_all(request):
    """
    Renders the About page
    lowercase name correlate with path in about/urls.py
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
