from django.shortcuts import render, redirect
from .models import Tutorial, Books, Post, Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

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

def register(request):
    if  request.method == "POST":
        form = UserCreationForm(request.POST)
        # check if form valid
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("personal:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request,
                  "personal/register.html",
                  context={"form":form})

# Blog
# Admin must be able to log in
# Restrict adding and editing posts to admin
# allow to view a blog post
# allow to comment on a blog post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'slug']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']

