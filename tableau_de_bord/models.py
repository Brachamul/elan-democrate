from django.db import models

class Email(models.Model):
    template = models.CharField(max_length=255) # what kind of email was it ? authentication? notification?
    author = models.CharField(max_length=255) # who sent it? the system ? a user?
    destination = models.EmailField() # who did we send it to ?
    date = models.DateTimeField(auto_now=True) # when was this ?