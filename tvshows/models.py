from django.db import models


class TVShow(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title
