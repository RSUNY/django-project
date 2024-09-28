from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.views import generic
from .models import Perfume, Duplicate, Review 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.

class PerfumesList(generic.ListView):
    model = Perfume
    template_name = "Perfumes/perfumes.html"
    context_object_name = 'perfumes'


class DuplicateList(generic.ListView):
    model = Duplicate
    template_name = "Perfumes/duplicates.html"
    context_object_name = 'duplicates'


class PerfumeDetail(generic.DetailView):
    model = Perfume
    template_name = "Perfumes/perfume_detail.html"
    context_object_name = 'perfume'
    paginate_by = 8


class DuplicateDetail(generic.DetailView):
    model = Duplicate
    template_name = "Perfumes/duplicate_detail.html"
    context_object_name = 'duplicate'
    paginate_by = 8

def PerfumeDetail(request, slug):
    """
    Display an individual :model:`Perfumes.Review`.

    **Context**

    ``post``
        An instance of :model:`Perfumes.Review`.

    **Post:method requiring instance=re**

    Edit Review`
    """
