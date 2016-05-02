from django.conf.urls import url
from teachers import views


urlpatterns = [
    url(r'^$', views.teachers, name='teachers'),
]