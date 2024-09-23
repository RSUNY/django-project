from django.db import models

# Create your models here.
class Poster(models.Model):
        title = models.CharField(max_length=50)
        # featured_image = CloudinaryField('image', default='placeholder')
