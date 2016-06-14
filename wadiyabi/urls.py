from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin

#handler404 = 'applications.websites.views.handler404'
#handler500 = 'applications.websites.views.handler500'
from applications.delivrem import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('applications.delivrem.urls')),
    url(r'^', include('applications.account.urls')),
]
#Static files serves with WhiteNoise (pip install WhiteNoise)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
