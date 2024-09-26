from django.db import models
from django.contrib.auth.models import User
from blog.models import PerfumesList
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.db.models.fields import DecimalField, FloatField, IntegerField

STATUS = ((0 , "Draft") , (1 ,"Published"))
# Create your models here.
class Perfume(models.Model):
        perfume_id = models.CharField()
        slug = models.SlugField()
        customer_id = models.ManyToManyField(PerfumesList)

        
        featured_image = CloudinaryField('image', default='placeholder')



class Review(models.Model):
        perfume_id = models.CharField(max_length=200, unique=True)
        featured_image = CloudinaryField('image', default='placeholder')
        status = models.IntegerField(choices=STATUS, default=0)

class Meta:
        ordering = ["-created_on"]

# related_query-__name__
# related _name 
# limit_choices_to
# choice_set 
# models.py 
# from django.db import models
# from django.utils import timezone
# from autoslug import AutoSlugField
# forms.py
# from django import forms
# from django.forms import ModelForm
# from app.models import UserProfile
# all 
# from django.contrib.auth.models import User



# Class UserProfile(models.Model)
#     user = models.OneToOneField(User)
#     website = models.URLField(blank=True)
#     picture = models.ImageField(uploade_to='media/' , blank=True)

#     def __unicode_(self):
#         return self.user.username


#     model = User
#     fields = ('username ' , 'email' , 'password')
# class UserProfileForm(forms)
#     class Meta:
#     model = UserProfile
#     fields = ('website' , 'picture')