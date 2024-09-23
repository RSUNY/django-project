from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from .models import Poster
from django.views import generic


# Create your views here.
class ComparisonList(generic.ListView):
    model = Poster