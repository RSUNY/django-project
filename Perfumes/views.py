from django.shortcuts import (
    render, get_object_or_404, redirect, reverse
)
from django.views import generic
from .models import Perfume, Duplicate, Review
from .forms import ReviewForm
from django.contrib import messages


class PerfumesList(generic.ListView):
    model = Perfume
    template_name = "perfumes.html"
    context_object_name = 'perfumes'
    paginate_by = 8


class PerfumeDetail(generic.View):
    def get(self, request, slug):
        perfume = self.get_perfume(slug)
        reviews = perfume.reviews.all().order_by("-created_on")
        reviews_count = perfume.reviews.filter(approved=True).count()
        review_form = ReviewForm()

        return render(
            request,
            "perfume_detail.html",
            {
                "perfume": perfume,
                "reviews": reviews,
                "reviews_count": reviews_count,
                "review_form": review_form,
            },
        )

    def post(self, request, slug):
        perfume = self.get_perfume(slug)
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            self.save_review(review_form, perfume, request.user)
            messages.success(request, 'Review has been submitted')
        else:
            messages.error(request, 'Error submitting review')

        return redirect('perfume_detail', slug=slug)

    def get_perfume(self, slug):
        queryset = Perfume.objects.filter(status=1)
        return get_object_or_404(queryset, slug=slug)

    def save_review(self, form, perfume, user):
        review = form.save(commit=False)
        review.reviewer_featured = user
        review.perfume = perfume
        review.save()


class DuplicatesList(generic.ListView):
    model = Duplicate
    template_name = "duplicates.html"
    context_object_name = 'duplicates'
    paginate_by = 8


class DuplicateDetail(generic.View):
    def get(self, request, slug):
        duplicate = self.get_duplicate(slug)
        reviews = duplicate.reviews.all().order_by("-created_on")
        reviews_count = duplicate.reviews.filter(approved=True).count()
        review_form = ReviewForm()

        return render(
            request,
            "duplicate_detail.html",
            {
                "duplicate": duplicate,
                "reviews": reviews,
                "reviews_count": reviews_count,
                "review_form": review_form,
            },
        )

    def post(self, request, slug):
        duplicate = self.get_duplicate(slug)
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            self.save_review(review_form, duplicate, request.user)
            messages.success(request, 'Review has been submitted')
        else:
            messages.error(request, 'Error submitting review')

        return redirect('duplicate_detail', slug=slug)

    def get_duplicate(self, slug):
        queryset = Duplicate.objects.filter(status=1)
        return get_object_or_404(queryset, slug=slug)

    def save_review(self, form, duplicate, user):
        review = form.save(commit=False)
        review.reviewer_featured = user
        review.duplicate = duplicate
        review.save()


# Review editing and deletion functions
def edit_review(request, slug, review_id):
    return handle_review_edit(request, slug, review_id, Perfume)


def delete_review(request, slug, review_id):
    return handle_review_delete(request, slug, review_id, Perfume)


def edit_duplicate_review(request, slug, review_id):
    return handle_review_edit(request, slug, review_id, Duplicate)


def delete_duplicate_review(request, slug, review_id):
    return handle_review_delete(request, slug, review_id, Duplicate)


def handle_review_edit(request, slug, review_id, model):
    instance = model.objects.filter(status=1).get(slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer_featured = request.user
            if model == Perfume:
                review.perfume = instance
            else:
                review.duplicate = instance
            review.save()
            messages.success(request, 'Review edited successfully')
        else:
            messages.error(request, 'Error updating Review!')

    return HttpResponseRedirect(reverse('perfume_detail' if model == Perfume else 'duplicate_detail', args=[slug]))


def handle_review_delete(request, slug, review_id, model):
    instance = model.objects.filter(status=1).get(slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.reviewer_featured == request.user:
        review.delete()
        messages.success(request, 'Review deleted!')
    else:
        messages.error(request, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('perfume_detail' if model == Perfume else 'duplicate_detail', args=[slug]))
