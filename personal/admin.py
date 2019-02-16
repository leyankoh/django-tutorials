from django.contrib import admin
from .models import Tutorial
# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    # override the fields order
    fields = ["tutorial_title",
              "tutorial_published",
              "tutorial_content"
              ]

admin.site.register(Tutorial, TutorialAdmin)