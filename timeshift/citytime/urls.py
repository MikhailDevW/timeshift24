# ice_cream/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('allcities/', views.allcities, name='all'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
