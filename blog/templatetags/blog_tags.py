from django import template
import math
from blog.models import Post, Category


register = template.Library()

@register.simple_tag
def hello(a=1):
    return math.pow(a, 2)

@register.simple_tag()
def count_posts():
    count_posts = Post.objects.filter(status=1).count()
    return count_posts

@register.simple_tag(name='t_posts')
def total_posts():
    posts = Post.objects.filter(status=1)
    return posts

@register.inclusion_tag('blog/latest-posts.html')
def latest_posts():
    posts = Post.objects.filter(status=1)[:3]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-category.html')
def post_category():
    posts = Post.objects.filter(status=1)
    cat_obj = Category.objects.all()
    cat_dict = {}
    for name in cat_obj:
        cat_dict[name] = posts.filter(category=name).count()
    return {'cat': cat_dict}
