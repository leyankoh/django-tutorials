from . import views
from django.urls import path

app_name = 'personal'
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('books/', views.books, name='books'),
]
