from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, "home.html", {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, "detail.html", {'blog_detail': blog_detail})

def new(request):
    return render(request, "new.html")

def submit(request):
    new = Blog()
    new.title= request.GET['title']
    new.body = request.GET['body']
    new.date = request.GET['day']
    new.who = request.GET['who']
    new.save()
    return redirect("/blog/"+str(new.id))
