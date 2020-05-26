from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Blog

def index(request):
    blogs = Blog.objects
    return render(request, 'index.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog_detail':blog_detail})

def create(request):
    return render(request, 'create.html')

def create_blog(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/' + str(blog.id))