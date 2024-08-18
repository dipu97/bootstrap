from django.db import models

# Create your models here.


class Carousels(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    image = models.ImageField(upload_to='carousel/')

    def __str__(self):
        return self.title
