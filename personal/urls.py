from . import views
from django.urls import path

app_name = 'personal'
urlpatterns = [
    path("", views.homepage, name="homepage"),

]
