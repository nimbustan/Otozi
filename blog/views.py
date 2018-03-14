from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Blog

# Create your views here.

def index(request):
    posts = Blog.objects.filter(create_time__lte=timezone.now()).order_by('create_time')
    return render(request, 'index.html',{'posts': posts})

def detay(request, url):
    val = Blog.objects.get(slug = url)
    return render(request, 'detay.html',locals())

