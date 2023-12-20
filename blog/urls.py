from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.all_posts, name='all-posts'),
    path('posts/<slug>', views.blog, name='blog-detail')
]