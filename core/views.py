from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def index(request):
    post = BlogPost.objects.first()
    return render(request, 'core/index.html', {"post": post})