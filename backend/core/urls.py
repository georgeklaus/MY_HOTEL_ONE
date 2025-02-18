from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index_html'),  # Add this line to match /index.html
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('faq.html', views.faq, name='faq'),
    path('services.html', views.services, name='services'),
    path('rooms.html', views.rooms, name='rooms'),
    path('news.html', views.news, name='news'),
    path('post.html', views.post, name='post'),
    path('restaurant.html', views.restaurant, name='restaurant'),
    path('room-details.html', views.room_details, name='room_details'),
    path('spa-wellness.html', views.spa_wellness, name='spa_wellness'),
]