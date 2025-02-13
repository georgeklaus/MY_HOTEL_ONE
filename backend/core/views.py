from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def careers(request):
    return render(request, 'careers.html')

def contact(request):
    return render(request, 'contact.html')

def facilities(request):
    return render(request, 'facilities.html')

def faq(request):
    return render(request, 'faq.html')

def gallery(request):
    return render(request, 'gallery.html')
