from django.shortcuts import render

#django-friendship
from django.contrib.auth.models import User
from friendship.models import Friend, Follow
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello world</h1>')
