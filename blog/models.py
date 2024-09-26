from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.fields import DecimalField, FloatField, IntegerField
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Subscriber(User):
    serial_number = models.DecimalField()
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    order = models.IntegerField(default=1)
    users = models.ManyToManyField(User, related_name='subscribers')

    

SUBS_CHOICES = (
    ('Entreprise', 'ent'),
    ('Professional', 'pro'),
    ('Free', 'free') 

)

class Subs(models.Model):
    slug = models.SlugField()
    sub_type =models.CharField(
    choices = SUBS_CHOICES,
    default = 'Free', max_length = 30)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='subscription')


    def __str__(self):
        return self.sub_type
    status = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @property
    def is_active(self):
        return self.status == "active" or self.status == "trialing"



class Article(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=100, unique=True)
    dupe_name = models.CharField(max_length=16)
    default_description = models.TextField()
     
    def save(self, **kwargs):
        if self.name == "":
            return f"{self.title} ({self.name})"
        else:
            super().save(**kwargs) 
                   