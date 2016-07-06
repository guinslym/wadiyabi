from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include, handler404, handler500


app_name = 'delivrem'
#handler404 = 'applications.websites.views.handler404'
#handler500 = 'applications.websites.views.handler500'
from applications.delivrem import views
from applications.delivrem.views import (
    ProductCreateView,
	)

urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='list'),
    url(r'^create/$', views.ProductCreateView.as_view(), name='create'),
     url(r'^product/new/$', views.ProductCreateView.as_view(), name='product_new'),
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', views.ProductUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.ProductDeleteView.as_view(), name='delete'),
]

#Static files serves with WhiteNoise (pip install WhiteNoise)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
