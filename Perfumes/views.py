from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.views import generic
# from .forms import ReviewForm
from .models import Perfume, Duplicate, Review 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Avg
# Create your views here.

class PerfumesList(generic.ListView):
    queryset = Perfume.objects.all()
    template_name = "index.html"