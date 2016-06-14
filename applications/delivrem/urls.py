from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('applications.delivrem.urls')),
]
