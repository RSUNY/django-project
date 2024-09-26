from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.db.models.fields import DecimalField, FloatField, IntegerField



STATUS = ((0 , "Draft") , (1 ,"Published"))
# Create your models here.
class Perfume(models.Model):
        perfume_id = models.CharField()
        slug = models.SlugField()
        title = models.CharField(max_length=200, unique=True)
        style = models.CharField(max_length=200)
        featured_original = CloudinaryField('image', default='placeholder')

class Duplicate(models.Model):
        perfume_id = models.CharField()
        slug = models.SlugField()
        title = models.CharField(max_length=200, unique=True)
        style = models.DecimalField(max_digits=10, decimal_places=2)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        origin = models.CharField(max_length=50)
        featured_image = CloudinaryField('image', default='placeholder')



class Review(models.Model):
        perfume_id = models.CharField(max_length=200, unique=True)
        featured_image = CloudinaryField('image', default='placeholder')
        status = models.IntegerField(choices=STATUS, default=0)
        review_title = models.CharField(max_length=50, unique = False)
        reviewer_featured = models.ForeignKey(
                User,on_delete=models.CASCADE, related_name="reviewer"
        )
        rating_approved = models.BooleanField(default=False)
        created_on = models.DateTimeField(auto_now_add=True)
        rating = models.IntegerField(
                validators=[MinValueValidator(1), MaxValueValidator(5)]
        
        )
class Meta:
        ordering = ["-created_on"]

def __str__(self):
        return f"Review of {self.perfume_id} by {self.reviewer_featured}"