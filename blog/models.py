from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.fields import DecimalField, FloatField, IntegerField

# Create your models here.
class PerfumesList(models.Model):
       article_name = models.OneToOneField(Duplicate,
        on_delete=models.CASCADE, parent_link=True, primary_key=True,)
       perfume = models.ForeignKey(
        Original, on_delete=models.CASCADE, related_name='perfumes_lists'
    )

# PerfumesList = {}

# class Article(Duplicate):
#        serial_number = models.DecimalField()
#        perfumes_list = models.ForeignKey()#Change name as needed
#        course = models.ForeignKey(Subs, on_delete=models.CASCADE, related_name='videos')
#        vimeo_id = models.CharField(max_length=50)
#        title = models.CharField(max_length=150)
#        slug = models.SlugField(unique=True)
#        description = models.TextField()
#        order = models.IntegerField(default=1)

# class Meta:
#         ordering = ["order"]    

# # other instances
       
# class Original(models.Model):
#     course = models.ForeignKey(Subs, on_delete=models.CASCADE, related_name='videos')
#     vimeo_id = models.CharField(max_length=50)
#     title = models.CharField(max_length=150)
#     slug = models.SlugField(unique=True)
#     description = models.TextField()
#     order = models.IntegerField(default=1)

# class Meta:
#         ordering = ["order"]    

# # other instances
    

#          # displays str(obj) in the admin site
# def get_absolute_url(self):
#         return reverse("content:video-detail", kwargs={
#             "video_slug": self.slug,
#             "slug": self.Subs.slug
#         })



# class Subs(models.Model):
#        slug = models.Slugfield()
#        def __str__(self):
#               return self.title




# class Poster(models.Model):
#         title = models.CharField(max_length=50)
#         name = models.CharField(max_length=100, unique=True)
#         dupe_name = models.CharField(max_length=16)

#         default_description = models.TextField()
#         # featured_image = CloudinaryField('image', default='placeholder')
#  #
#         #     class Target(models.Model):
#         #         model = models.IntegerField()
#         #         model_set = models.IntegerField()
#         #
#         #     class Model(models.Model):
#         #         foreign = models.ForeignKey(Target)
#         #         m2m = models.ManyToManyField(Target)
        