from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^visits/', include('visits.urls', namespace='visits')),
]