from django.shortcuts import render
from .models import Blog


def blogs(request):
    blog = Blog.objects.all()
    context = {'blogs': blog}
    return render(request, 'Blog/blogs.html', context)


def singleBlog(request, pk):
    # blog = Blog.objects.get(id=pk)
    # context = {'blog': blog}
    return render(request, 'Blog/single-blog.html')
