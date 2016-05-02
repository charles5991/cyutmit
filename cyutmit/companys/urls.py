from django.conf.urls import url
from companys import views


urlpatterns = [
    url(r'^$', views.teachers, name='companys'),
]