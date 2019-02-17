from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial, Books

# Create your views here.
def index(request): #always pass request to be explicit
    return render(request, 'personal/home.html')

def homepage(request): # always pass request for a view
    return render(request = request,
                  template_name="personal/home.html",
                  context={"tutorials": Tutorial.objects.all})

def books(request):
    return render(request=request,
                  template_name="personal/books.html",
                  context={"books": Books.objects.all})