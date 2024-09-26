from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from .models import Article, Subs, Subscriber
from django.views import generic


# Create your views here.
class ComparisonList(generic.ListView):
    model = object

    # single blog detail event is clicked on to view
# def event_detail(request, event_id):
#     template = "events/event_detail.html"
#     event= get_object_or_404(Event, event_id=int)

#     return render(
#         request,
#         template,
#         {"details": event},
    # )

def blog_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Poster.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/blog_detail.html",
        {"post": post},
    )