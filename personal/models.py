from django.db import models
from datetime import datetime
# Create your models here.
# remember makemigrations > migrate manage.py
class Tutorial(models.Model):
    # add column
    tutorial_title = models.CharField(max_length=200) # google django model fields as a reference
    tutorial_content = models.TextField() # use this for information of infinite length
    tutorial_published = models.DateTimeField("Date Published", default=datetime.now)

    # override string method
    def __str__(self):
        return self.tutorial_title

    # model will map to db table


class Books(models.Model):

    book_title = models.CharField(max_length=200)
    book_published = models.DateTimeField("Date Published")
    book_description = models.TextField()

    def __str__(self):
        return self.book_title