from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.urlresolvers import reverse_lazy

#django-friendship
from django.contrib.auth.models import User
from friendship.models import Friend, Follow

from django.utils.decorators import method_decorator
from django.views.generic import edit, DetailView, ListView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .decorators import staff_or_author_required

from django.core.urlresolvers import reverse

from .utils import (
    is_staff,
    SuccessMessageMixin,
    StaffMixin
)
from . import models
from .forms import (
        ProductForm,
        ProductEditForm
    )
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

    def get_queryset(self):
        return Product.objects.all()#filter(status__iexact=Article.STATUS.active)

    def get_paginate_by(self, queryset):
        """ Paginate by specified value in querystring, or use default class property value.  """
        return self.request.GET.get('paginate_by', self.paginate_by)

class ProductCreateView(SuccessMessageMixin, CreateView):
    form_class = ProductForm
    template_name = "product_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super(ProductCreateView, self).form_valid(form)

product_new = login_required(ProductCreateView.as_view())

class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = "product_update.html"

    #@method_decorator(login_required)
    #@method_decorator(staff_or_author_required(Product))
    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #migh need to remove that line
        self.object.author = self.request.user
        return super(self.__class__, self).form_valid(form)

post_edit = ProductUpdateView.as_view()

"""
class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context
"""

class ProductDetailView(DetailView):
    template_name = "detail.html"
    model = Product
    """
    #TODO the retrun home button doesn't display all the Product list
    """


class  ProductDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    template_name = '_delete_confirm.html'

    #@method_decorator(login_required)
    #@method_decorator(staff_or_author_required(Product))
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['back_page'] = reverse_lazy('delivrem:product-home')
        return context

    def get_success_url(self):
        return reverse_lazy('delivrem:product-home')

product_delete = ProductDeleteView.as_view()



class HomeView(TemplateView):
    template_name = 'home.html'
