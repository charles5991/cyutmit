from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^visits/', include('visits.urls', namespace='visits')),
    url(r'^sysSettings/', include('sysSettings.urls', namespace='sysSettings')),
    url(r'^teachers/', include('teachers.urls', namespace='teachers')),
    url(r'^companys/', include('companys.urls', namespace='companys')),
]