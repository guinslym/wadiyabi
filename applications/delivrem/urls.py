from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include, handler404, handler500


app_name = 'delivrem'
#handler404 = 'applications.websites.views.handler404'
#handler500 = 'applications.websites.views.handler500'
from applications.delivrem import views


from .views import (
        ProductListView,
        ProductCreateView,
        ProductDetailView,
        ProductUpdateView,
        ProductDeleteView,
)

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='product-home'),
    url(r'^create/$', ProductCreateView.as_view(), name='product-create'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product-detail'),
    url(r'^update/(?P<pk>\d+)/$', ProductUpdateView.as_view(), name='product-update'),
    url(r'^sell-it/(?P<pk>\d+)/$', ProductUpdateView.as_view(), name='product-sell-it'),
    url(r'^delete/(?P<pk>\d+)/$', ProductDeleteView.as_view(), name='product-delete'),
]

#Static files serves with WhiteNoise (pip install WhiteNoise)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
