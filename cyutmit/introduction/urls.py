from django.conf.urls import url
from introduction import views

urlpatterns = [
    url(r'^$', views.introduction, name='introduction'),
    url(r'^(?P<introductionId>[0-9]+)/$', views.viewIntroduction, name='viewIntroduction'),
    url(r'addIntroduction/', views.introduction, name='addIntroduction'),
    url(r'editIntroduction/(?P<introductionId>[0-9]+)/$', views.editIntroduction, name='editIntroduction'),
]
