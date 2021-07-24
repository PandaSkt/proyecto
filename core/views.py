from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def shop(request):
    return render(request, 'core/shop.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def login(request):
    return render(request, 'core/login.html')

def register(request):
    return render(request, 'core/register.html')