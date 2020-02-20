from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('register/', views.register, name='register'),
    url('submit/', views.submit, name='submit'),
    url('profile/', views.profile, name='profile'),
   


]
