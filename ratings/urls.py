from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('register/', views.register, name='register'),
    url('profile/', views.profile, name='profile'),


]
