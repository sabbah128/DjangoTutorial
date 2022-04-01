from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)

    return render(request, 'blog/blog-home.html', {'posts': posts})


def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    return render(request, 'blog/blog-single.html', {'post': post})


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'): # py 3.8 walrus
            posts = posts.filter(content__contains=s)
    return render(request, 'blog/blog-home.html', {'posts': posts})


# def blog_category(request, cat_name):
#     posts = Post.objects.filter(status=1)
#     posts = posts.filter(category__name=cat_name)
#     return render(request, 'blog/blog-home.html', {'posts': posts})
