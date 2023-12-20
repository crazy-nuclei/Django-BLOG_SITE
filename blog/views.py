from django.http import HttpResponse
from django.shortcuts import render


posts = [
    {
        'slug': 'first-post',
        'title': 'First Post Title',
        'excerpt': 'This is the excerpt for the first post.',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...'
    },
    {
        'slug': 'second-post',
        'title': 'Second Post Title',
        'excerpt': 'This is the excerpt for the second post.',
        'content': 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ...'
    },
    {
        'slug': 'third-post',
        'title': 'Third Post Title',
        'excerpt': 'This is the excerpt for the third post.',
        'content': 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris... '
    },
    {
        'slug': 'fourth-post',
        'title': 'Fourth Post Title',
        'excerpt': 'This is the excerpt for the fourth post.',
        'content': 'Duis aute irure dolor in reprehenderit in voluptate velit esse... '
    },
    {
        'slug': 'fifth-post',
        'title': 'Fifth Post Title',
        'excerpt': 'This is the excerpt for the fifth post.',
        'content': 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui... '
    },
    {
        'slug': 'sixth-post',
        'title': 'Sixth Post Title',
        'excerpt': 'This is the excerpt for the sixth post.',
        'content': 'Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit... '
    }
]


# Create your views here.
def index(request): 
    latest_posts = posts[-3:]
    return render(request, 'blog/index.html',{
        "posts": latest_posts
    })


def all_posts(request): 
    return render(request, 'blog/allBlogs.html', {
        'posts': posts
    })

def blog(request, slug): 
    post = None
    for pos in posts: 
        if pos['slug'] == slug: 
            post = pos
            break
    return render(request, 'blog/blog.html', {
        'post': post
    })