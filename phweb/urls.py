from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'home/', views.home, name='home'),
    url(r'gallery/', views.gallery, name='gallery'),
]