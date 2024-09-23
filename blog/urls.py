from django.urls import path
from . import views


urlpatterns = [
    path('', views.ComparisonList.as_view(), name='home'),
    path('<slug:slug>', views.blog_detail.html, name="blog_detai")
]