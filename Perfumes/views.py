from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.views import generic
from .models import Perfume, Duplicate, Review 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
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


@login_required
def review_edit(request, slug, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
    if form.is_valid():
        form.save()
    return redirect('perfume_detail', slug=slug)
    else:
        form = ReviewForm(instance=review)
    return redirect('perfume_detail',
slug=slug)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review_edit.html', {'form': form})
    """
    Display an individual :model:`Perfumes.Review`.

    **Context**

    ``post``
        An instance of :model:`Perfumes.Review`.

    **Post:method requiring instance=re**

    Edit Review`
    """
