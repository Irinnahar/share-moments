from django.db import models
from django.urls import reverse

# Create your models here.
class Gallery(models.Model):
    image_name = models.CharField(max_length = 250)
    image_type = models.CharField(max_length = 250)
    image_logo = models.ImageField()

    def get_absolute_url(self):
        return reverse('gallery:index', kwargs={'pk': self.pk})

    def __str__(self):
        return self.image_name
