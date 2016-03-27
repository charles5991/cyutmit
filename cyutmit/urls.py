from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('visits.urls')),
    url(r'^visits/', include('visits.urls', namespace='visits')),
]