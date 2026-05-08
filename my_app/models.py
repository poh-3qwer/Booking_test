from django.db import models

# Create your models here.

class LibraryBook(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    isbn = models.CharField(max_length=60)
    aviable = models.BooleanField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['author']
        unique_together = (('title', 'isbn'),)