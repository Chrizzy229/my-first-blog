# defines all objects called Models

from django.conf import settings
from django.db import models
from django.utils import timezone

# Post is a Django model so Django knows it should be saved in the Database
class Post(models.Model):
    # link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # define text with a limited number of characters
    title = models.CharField(max_length=200)

    # long text without a limit eg a blog post
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # functions that belong to the Post class
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
