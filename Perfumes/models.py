from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

STATUS = ()
# Create your models here.
class Perfume(models.Model):
        featured_image = CloudinaryField('image', default='placeholder')

class Review(models.Model):
        featured_image = CloudinaryField('image', default='placeholder')
    # …

class Meta:
        ordering = ["-created_on"]