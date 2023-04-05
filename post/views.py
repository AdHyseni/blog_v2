from django.shortcuts import render,get_object_or_404
from .models import Autori, Post

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def blog(request):
    postimet = Post.objects.all()
    context = {'postimet':postimet}
    return render(request,'blog/blog.html',context)