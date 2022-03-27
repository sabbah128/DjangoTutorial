from django.shortcuts import render


content = {'name': 'Hossein', 'lname': 'KianAra', 'job': 'ML & BackEnd'}
def blog_view(request):
    return render(request, 'blog/blog-home.html', content)


def blog_single(request):
    return render(request, 'blog/blog-single.html')
    
