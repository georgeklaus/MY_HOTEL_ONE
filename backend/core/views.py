from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def services(request):
    return render(request, 'services.html')

def rooms(request):
    return render(request, 'rooms.html')

def news(request):
    return render(request, 'news.html')

def post(request):
    return render(request, 'post.html')

def restaurant(request):
    return render(request, 'restaurant.html')

def room_details(request):
    return render(request, 'room_details.html')

def spa_wellness(request):
    return render(request, 'spa_wellness.html')