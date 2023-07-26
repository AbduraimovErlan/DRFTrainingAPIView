from django.db import models

class Book2(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()

    def __str__(self):
        return self.title