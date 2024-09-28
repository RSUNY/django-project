from django.urls import path
from . import views
from django.shortcuts import render
from django.http import HttpResponse
urlpatterns = [
    path('perfumes/', views.PerfumesList.as_view(), name='Perfumes'),
    path('duplicates/', views.DuplicatesList.as_view(), name='Duplicates'),
    path('<slug:slug>/', views.PerfumeDetail.as_view(), name='perfume_detail'),
    path('<slug:slug>/', views.DuplicateDetail.as_view(), name='duplicate_detail'),

   
     path(
        '<slug:slug>/edit_review/<int:review_id>',
        views.edit_review,
        name='edit_review'
    ),
   #  edit reviews
    path(
        '<slug:slug>/delete_review/<int:review_id>',
        views.delete_review,
        name='delete_review'
    ),
    # delete review
]


# added urls to view home review_edit in views and review_delete
