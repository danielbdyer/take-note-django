from __future__ import unicode_literals

from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField('Label', related_name='notes')

    # Will return the title of the note as the string representation of it
    def __str__(self):
        return self.title


class Label(models.Model):
    text = models.CharField(max_length=200, default="")
    background_color = models.CharField(max_length=6, default="ffffff")
    text_color = models.CharField(max_length=6, default="000000")

    def __str__(self):
        return self.text
