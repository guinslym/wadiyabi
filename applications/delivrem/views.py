from django.shortcuts import render

#django-friendship
from django.contrib.auth.models import User
from friendship.models import Friend, Follow
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic


from . import models
from . import forms

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello world</h1>')


class HomeView(generic.TemplateView):
    template_name = 'home.html'
