from django.urls import path
from . import views

urlpatterns = [
    # lowercase view.name correlate with view created in about/views.py
    path('', views.about_all, name='about'),
]
