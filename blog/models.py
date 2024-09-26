from django.db import models
from Perfumes.models import Perfume
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.db.models.fields import DecimalField, FloatField, IntegerField

# Create your models here.
class Duplicate(PerfumesList):
       self_related_name = models.BigAutoField(primary_key=True)
# class  User(models.Modal):

class PerfumesList(Duplicate):
       article_name = models.OneToOneField(
              Piece, on_delete=models.CASCADE, parent_link=True)
              PerfumesList = PerfumesList()
       

PerfumesList = {}
# class list ModelForm()
#        serial_numeber = model.DecimalField()



# class Subs(models.ManyToManyField):




class Poster(models.Model):
        title = models.CharField(max_length=50)
        name = models.CharField(max_length=100, unique=True)
        dupe_name = models.CharField(max_length=16)

        default_description = models.TextField()
        # featured_image = CloudinaryField('image', default='placeholder')
 #
        #     class Target(models.Model):
        #         model = models.IntegerField()
        #         model_set = models.IntegerField()
        #
        #     class Model(models.Model):
        #         foreign = models.ForeignKey(Target)
        #         m2m = models.ManyToManyField(Target)
        