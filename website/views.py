from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post


def home_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def test(request):
    return render(request, 'test.html')

def latest_posts(request):
    posts = Post.objects.filter(status=1)
    return render(request, 'website/latest-blog.html', {'posts': posts})


