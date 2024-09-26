from django.contrib import admin
from .models import Perfume, Duplicate, Review



admin.site.register(Perfume)
admin.site.register(Duplicate)
admin.site.register(Review)


# Register your models here.
# @admin.register(Review)