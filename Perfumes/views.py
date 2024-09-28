from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.views import generic
# from .forms import ReviewForm
from .models import Perfume, Duplicate, Review 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Avg
# Create your views here.

class PerfumesList(generic.DetailView):
    queryset = Perfume.objects.all()
    template_name = "perfume_detail.html"


class DuplicateList(generic.DetailView):
    queryset = Perfume.objects.all()
    template_name = "duplicate_detail.html"


class Perfume_detail(generic.ListView):
    model = Perfume
    template_name = "blog/perfume_detail"
    paginate_by = 8


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post},)