from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include, handler404, handler500

#handler404 = 'applications.websites.views.handler404'
#handler500 = 'applications.websites.views.handler500'
from applications.delivrem import views
from applications.delivrem.views import (
	#post_list,
	#post_create,
	#post_detail,
	#post_update,
	#post_delete,
    #add_bulletin,
    ProductCreateView,
	)

urlpatterns = [
	#url(r'^$', post_list, name='list'),
    #url(r'^$', views.HomeView.as_view(), name='home'),
    #url(r'^$', add_bulletin, name="add_bulletin"),
    url(r'^$', ProductCreateView.as_view()),
    #url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    #url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
    url(r'^$', views.ProductListView.as_view(), name='list'),
    url(r'^create/$', views.ProductCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', views.ProductUpdateView.as_view(), name='update'),
]


'''
urlpatterns = [
    #url(r'^$', views.hello, name='hello'),
    #url(r'^history/$', views.snippet_history, name='snippet_history'),
    #url(r'^delete/$', views.snippet_delete, name='snippet_delete'),
    #url(r'^(?P<snippet_id>[a-zA-Z0-9]{%d,})/delete/$' % L, views.snippet_delete, name='snippet_delete'),
    url(r'^$', views.HomeView.as_view(), name='home'),
]
'''
#Static files serves with WhiteNoise (pip install WhiteNoise)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
