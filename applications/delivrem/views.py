from django.shortcuts import render
try:
    from urllib.parse import quote_plus #python 3
except:
    pass


from datetime import datetime
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

#django-friendship
from django.contrib.auth.models import User
from friendship.models import Friend, Follow

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import edit, DetailView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.conf import settings
from .decorators import staff_or_author_required


from . import models
from . import forms
from .forms import ProductForm
from .models import Product
#from .models import Post

#ClassView Add/Edit/Delete

def is_staff(user):
    return user and not user.is_anonymous() and user.is_staff

class StaffMixin(object):
    @method_decorator(login_required)
    @method_decorator(user_passes_test(is_staff))
    def dispatch(self, *args, **kwargs):
        return super(StaffMixin, self).dispatch(*args, **kwargs)

class MessageMixin(object):
    """
    Display notifications when using Class-Based Views
    """
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).form_valid(form)

class ProductListView(generic.ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['static_url'] = settings.STATIC_URL.rstrip('/')
        context['domain'] = Site.objects.get_current().domain
        context['now'] = datetime.now()
        return context

    def get_queryset(self):
        return Product.objects.all()#filter(status__iexact=Article.STATUS.active)

    def get_paginate_by(self, queryset):
        """ Paginate by specified value in querystring, or use default class property value.  """
        return self.request.GET.get('paginate_by', self.paginate_by)

class ProductCreateView(MessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = '_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.ip = self.request.META['REMOTE_ADDR']
        return super(self.__class__, self).form_valid(form)

product_new = login_required(ProductCreateView.as_view())

class ProductUpdateView(MessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = '_form.html'

    @method_decorator(login_required)
    @method_decorator(staff_or_author_required(Product))
    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.ip = self.request.META['REMOTE_ADDR']
        return super(self.__class__, self).form_valid(form)

post_edit = ProductUpdateView.as_view()


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['static_url'] = settings.STATIC_URL.rstrip('/')
        context['domain'] = Site.objects.get_current().domain
        context['now'] = datetime.now()
        return context



class  ProductDeleteView(MessageMixin, DeleteView):
    model = Product
    template_name = '_delete_confirm.html'

    @method_decorator(login_required)
    @method_decorator(staff_or_author_required(Product))
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['back_page'] = reverse_lazy('delivrem:index')
        return context

    def get_success_url(self):
        return reverse_lazy('delivrem:index')

product_delete = ProductDeleteView.as_view()

class HomeView(generic.TemplateView):
    template_name = 'home.html'
