from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post
from website.forms import CantactForm, NewsletterForm


def home_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = CantactForm(request.POST)
        if form.is_valid():
            form.save()
    form = CantactForm()
    return render(request, 'website/contact.html', {'form': form})

def latest_posts(request):
    posts = Post.objects.filter(status=1)
    return render(request, 'website/latest-blog.html', {'posts': posts})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def test(request):
    if request.method == 'POST':
        form = CantactForm(request.POST)
        if form.is_valid():
            # form.save()
            return HttpResponse('Thank you for your message.')
    form = CantactForm()
    return render(request, 'test.html', {'form': form})