from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post


# Create your views here.
def base(request):  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            context = {
                'message':'Invalid Credentials',
            }
            return render(request, 'base.html', context)
    return render(request, 'base.html')

def logout_view(request):
    logout(request)
    return render(request, 'base.html')
    
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('base'))
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    posts = Post.objects.all()
    
    return render(request, 'blog.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = Post.objects.get(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'detail.html', {'post': post})

def sign(request):
    return render(request, 'signup.html')
