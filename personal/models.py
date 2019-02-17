from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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

# make model for a blog
# https://www.agiliq.com/books/djenofdjango/chapter4.html (guide - quite outdated though)
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True) # store slugs (for SEO?)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('blog_post_detail', [self.slug,])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) # get a slug from the string.
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    name = models.CharField(max_length = 42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

