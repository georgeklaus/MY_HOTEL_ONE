from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('services/', views.services, name='services'),
    path('rooms/', views.rooms, name='rooms'),
    path('news/', views.news, name='news'),
    path('post/', views.post, name='post'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('room-details/', views.room_details, name='room_details'),
    path('spa-wellness/', views.spa_wellness, name='spa_wellness'),
]