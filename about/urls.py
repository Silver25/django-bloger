from . import views
from django.urls import path

urlpatterns = [
    # lowercase view.name correlate with view created in about/views.py
    path('', views.about_all, name='about'),
]