from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)   # Short text
    content = models.TextField()               # Long text

    def __str__(self):
        return self.title
