from django.db import models
from Perfumes.models import Perfume

# Create your models here.
class Poster(models.Model):
        title = models.CharField(max_length=50)
        name = models.CharField(max_length=100)
        tagline = models.TextField()
        # featured_image = CloudinaryField('image', default='placeholder')
 #
        #     class Target(models.Model):
        #         model = models.IntegerField()
        #         model_set = models.IntegerField()
        #
        #     class Model(models.Model):
        #         foreign = models.ForeignKey(Target)
        #         m2m = models.ManyToManyField(Target)
        