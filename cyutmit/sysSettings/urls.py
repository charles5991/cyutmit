from django.conf.urls import url
from sysSettings import views


urlpatterns = [
    url(r'^$', views.sysSettings, name='sysSettings'),
]