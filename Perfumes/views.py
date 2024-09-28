from django.shortcuts import (
    render, get_object_or_404, redirect, reverse
)
from django.views.generic import TemplateView
from django.views import generic
from .models import Perfume, Duplicate, Review
from .forms import ReviewForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Avg

# Create your views here.
class PerfumesList(generic.ListView):
    model = Perfume.objects.all()
    template_name = "Perfumes/perfumes.html"
    context_object_name = 'perfumes'
    paginate_by = 8


def PerfumeDetail(request, slug):
    queryset = Perfume.objects.filter(status=1)
    perfume = get_object_or_404(queryset, slug=slug)
    reviews = beer.reviews.all().order_by("-created_on")
    reviews_count = beer.reviews.filter(approved=True).count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer_featured = request.user
            review.review_title = review_form.cleaned_data.get('review_title')
            review.review_content = review_form.cleaned_data.get(
                'review_content'
            )
            review.rating = review_form.cleaned_data.get('rating')
            review.perfume_id = beer
            review.save()
            messages.add_message(
                request, messages.SUCCESS, 'Review has been submitted'
            )

            return redirect('beer_detail', slug=slug)
    else:
        review_form = ReviewForm()

    return render(
        request,
        "beer_detail.html",
        {
            "beer": beer,
            "reviews": reviews,
            "reviews_count": reviews_count,
            "review_form": review_form,
            "average_rating": average_rating,
        },
    )


def review_edit(request, slug, review_id):
    if request.method == "POST":
        queryset = Beer.objects.filter(status=1)
        beer = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.poster = request.user
            review.review_title = review_form.cleaned_data.get(
                'review_title'
            )
            review.review_content = review_form.cleaned_data.get(
                'review_content'
            )
            review.rating = review_form.cleaned_data.get('rating')
            review.beer_name = beer
            review.save()
            messages.add_message(
                request, messages.SUCCESS, 'Review edited successfully'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating Review!'
            )
    return HttpResponseRedirect(reverse('beer_detail', args=[slug]))


def review_delete(request, slug, review_id):
    queryset = Beer.objects.filter(status=1)
    beer = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.poster == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own reviews!'
        )

    return HttpResponseRedirect(reverse('beer_detail', args=[slug]))


class DuplicatesList(generic.ListView):
    model = Duplicate.objects.all()
    template_name = "Perfumes/duplicates.html"
    context_object_name = 'duplicates'
    paginate_by = 8


    def get_queryset(self):
        # Annotate each beer with its average rating
        return Beer.objects.filter(status=1).annotate(
            average_rating=Avg('reviews__rating')
        ).order_by('beer_name')


def beer_detail(request, slug):
    queryset = Beer.objects.filter(status=1)
    beer = get_object_or_404(queryset, slug=slug)
    reviews = beer.reviews.all().order_by("-created_on")
    reviews_count = beer.reviews.filter(approved=True).count()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.poster = request.user
            review.review_title = review_form.cleaned_data.get('review_title')
            review.review_content = review_form.cleaned_data.get(
                'review_content'
            )
            review.rating = review_form.cleaned_data.get('rating')
            review.beer_name = beer
            review.save()
            messages.add_message(
                request, messages.SUCCESS, 'Review has been submitted'
            )

            return redirect('beer_detail', slug=slug)
    else:
        review_form = ReviewForm()

    return render(
        request,
        "beer_detail.html",
        {
            "beer": beer,
            "reviews": reviews,
            "reviews_count": reviews_count,
            "review_form": review_form,
            "average_rating": average_rating,
        },
    )


def review_edit(request, slug, review_id):
    if request.method == "POST":
        queryset = Beer.objects.filter(status=1)
        beer = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.poster = request.user
            review.review_title = review_form.cleaned_data.get(
                'review_title'
            )
            review.review_content = review_form.cleaned_data.get(
                'review_content'
            )
            review.rating = review_form.cleaned_data.get('rating')
            review.beer_name = beer
            review.save()
            messages.add_message(
                request, messages.SUCCESS, 'Review edited successfully'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating Review!'
            )
    return HttpResponseRedirect(reverse('beer_detail', args=[slug]))


def review_delete(request, slug, review_id):
    queryset = Beer.objects.filter(status=1)
    beer = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.poster == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own reviews!'
        )

    return HttpResponseRedirect(reverse('beer_detail', args=[slug]))


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





    """
    Display an individual :model:`Perfumes.Review`.

    **Context**

    ``post``
        An instance of :model:`Perfumes.Review`.

    **Post:method requiring instance=re**

    Edit Review`
    """
