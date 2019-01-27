from django.shortcuts import render

# Create your views here.
def index(request): #always pass request to be explicit
    return render(request, 'personal/home.html')