from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView, DetailView, ListView
from .models import Article, Subs, Subscriber
from django.views import generic


# Create your views here.
class ComparisonList(generic.ListView):
    model = object

 
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    class SiteView(ListView):
        queryset = Site
        template_name = "blog/index.html"

    class articles_detail(TemplateView):
        context_object_name = 'pageNum'
        template_name = 'blog/subscription_list.html'
    def _get_page(self, *args, **kwargs):