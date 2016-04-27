from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^(?P<newsId>[0-9]+)/$', views.viewNews, name='viewNews'),
    url(r'searchNews/', views.searchNews, name='searchNews'),
    url(r'addNews/', views.addNews, name='addNews'),
    url(r'editNews/(?P<newsId>[0-9]+)/$', views.editNews, name='editNews'),
    url(r'deleteNews/(?P<newsId>[0-9]+)/$', views.deleteNews, name='deleteNews'),
]
