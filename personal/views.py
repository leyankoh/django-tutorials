from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #always pass request to be explicit
    return render(request, 'personal/home.html')

def homepage(request): # always pass request for a view
    return HttpResponse("Mudkips")