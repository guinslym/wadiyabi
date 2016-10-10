"""lineez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include, handler404, handler500
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
     url(r'^friendship/', include('friendship.urls'))
    url(r'^', include('applications.delivrem.urls', namespace='delivrem')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# I need to set MEDIA_URL and MEDIA_ROOT in url
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
urlpatterns = patterns(''
    ...
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^secret/', include(admin.site.urls)),
)
'''
