from django.urls import path
from . import views
from django.shortcuts import render
from django.http import HttpResponse
urlpatterns = [
    
   path('', views.PerfumesList.as_view(), name='Perfumes'),
   path('', views.DuplicateList.as_view(), name='Duplicates'),
     path(
        '<slug:slug>/edit_review/<int:review_id>',
        views.review_edit,
        name='review_edit'
    ),
    path(
        '<slug:slug>/delete_review/<int:review_id>',
        views.review_delete,
        name='review_delete'
    ),
]

# added urls to view home review_edit in views and review_delete