from django.shortcuts import (
    render, get_object_or_404, redirect, reverse
)
from django.views import generic, View
from .models import Perfume, Duplicate, Review
from .forms import ReviewForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
class PerfumesList(generic.ListView):
    model = Perfume
    template_name = "Perfumes/perfumes.html"
    context_object_name = 'perfumes'
    paginate_by = 8


class PerfumeDetail(View):
    def get(self, request, slug):
        queryset = Perfume.objects.filter(status=1)
        perfume = get_object_or_404(queryset, slug=slug)
        reviews = perfume.reviews.all().order_by("-created_on")
        reviews_count = perfume.reviews.filter(approved=True).count()
        review_form = ReviewForm()
        
        return render(
            request,
            "Perfumes/perfume_detail.html",  # Use a specific template for detail view
            {
                "perfume": perfume,
                "reviews": reviews,
                "reviews_count": reviews_count,
                "review_form": review_form,
            },
        )

    def post(self, request, slug):
        queryset = Perfume.objects.filter(status=1)
        perfume = get_object_or_404(queryset, slug=slug)
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer_featured = request.user
            review.review_title = review_form.cleaned_data.get('review_title')
            review.review_content = review_form.cleaned_data.get('review_content')
            review.rating = review_form.cleaned_data.get('rating')
            review.perfume = perfume  # Correct foreign key assignment
            review.save()
            messages.success(request, 'Review has been submitted')
            return redirect('perfume_detail', slug=slug)

        messages.error(request, 'Error submitting review')
        return redirect('perfume_detail', slug=slug)


class DuplicatesList(generic.ListView):
    model = Duplicate
    template_name = "Perfumes/duplicates.html"
    context_object_name = 'duplicates'
    paginate_by = 8


class DuplicateDetail(View):
    def get(self, request, slug):
        queryset = Duplicate.objects.filter(status=1)
        duplicate = get_object_or_404(queryset, slug=slug)
        reviews = duplicate.reviews.all().order_by("-created_on")
        reviews_count = duplicate.reviews.filter(approved=True).count()
        review_form = ReviewForm()

        return render(
            request,
            "Perfumes/duplicate_detail.html",  # Use a specific template for detail view
            {
                "duplicate": duplicate,
                "reviews": reviews,
                "reviews_count": reviews_count,
                "review_form": review_form,
            },
        )

    def post(self, request, slug):
        queryset = Duplicate.objects.filter(status=1)
        duplicate = get_object_or_404(queryset, slug=slug)
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer_featured = request.user
            review.review_title = review_form.cleaned_data.get('review_title')
            review.review_content = review_form.cleaned_data.get('review_content')
            review.rating = review_form.cleaned_data.get('rating')
            review.duplicate = duplicate  # Correct foreign key assignment
            review.save()
            messages.success(request, 'Review has been submitted')
            return redirect('duplicate_detail', slug=slug)

        messages.error(request, 'Error submitting review')
        return redirect('duplicate_detail', slug=slug)


# Review editing and deletion should be outside the classes
def edit_review(request, slug, review_id):
    queryset = Perfume.objects.filter(status=1)
    perfume = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer_featured = request.user
            review.review_title = review_form.cleaned_data.get('review_title')
            review.rating = review_form.cleaned_data.get('rating')
            review.perfume = perfume
            review.save()
            messages.success(request, 'Review edited successfully')
        else:
            messages.error(request, 'Error updating Review!')

    return HttpResponseRedirect(reverse('perfume_detail', args=[slug]))


def delete_review(request, slug, review_id):
    queryset = Perfume.objects.filter(status=1)
    perfume = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.reviewer_featured == request.user:
        review.delete()
        messages.success(request, 'Review deleted!')
    else:
        messages.error(request, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('perfume_detail', args=[slug]))


def edit_duplicate_review(request, slug, review_id):
    queryset = Duplicate.objects.filter(status=1)
    duplicate = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer_featured = request.user
            review.review_title = review_form.cleaned_data.get('review_title')
            review.rating = review_form.cleaned_data.get('rating')
            review.duplicate = duplicate
            review.save()
            messages.success(request, 'Review edited successfully')
        else:
            messages.error(request, 'Error updating Review!')

    return HttpResponseRedirect(reverse('duplicate_detail', args=[slug]))


def delete_duplicate_review(request, slug, review_id):
    queryset = Duplicate.objects.filter(status=1)
    duplicate = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.reviewer_featured == request.user:
        review.delete()
        messages.success(request, 'Review deleted!')
    else:
        messages.error(request, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('duplicate_detail', args=[slug]))

    """
    Display an individual :model:`Perfumes.Review`.

    **Context**

    ``post``
        An instance of :model:`Perfumes.Review`.

    **Post:method requiring instance=re**

    'Delete:Edit Review Edit:Edit Review` 
    """
