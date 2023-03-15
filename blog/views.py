from django.shortcuts import render

def single(request):
    return render(request, 'blog/single.html')

def blog(request):
    return render(request, 'blog/blog.html')