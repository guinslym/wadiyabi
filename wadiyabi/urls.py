#from django.conf.urls.static import static
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin

#handler404 = 'applications.delivrem.views.handler404'
#handler500 = 'applications.delivrem.views.handler500'
from applications.delivrem import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('applications.delivrem.urls', namespace='delivrem')),
    url(r'^account/', include('applications.account.urls')),
    url('social-auth/',include('social.apps.django_app.urls', namespace='social')),
]
#Static files serves with WhiteNoise (pip install WhiteNoise)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls import static
if settings.DEBUG:

    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += \
        static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += \
        static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
