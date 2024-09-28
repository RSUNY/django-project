from django.urls import path
from . import views
from django.shortcuts import render
from django.http import HttpResponse
from .views import PerfumesList, DuplicatesList, PerfumeDetail, DuplicateDetail
from django.urls import path
from . import views

urlpatterns = [
   path('', views.PerfumesList.as_view(), name='perfumes_list'),
   path('', views.DuplicatesList.as_view(), name='duplicates_list'),
    
   path('perfumes/<slug:slug>/', views.PerfumeDetail.as_view(), name='perfume_detail'),
   path('duplicates/<slug:slug>/', views.DuplicateDetail.as_view(), name='duplicate_detail'),
    
   path('perfumes/<slug:slug>/edit_review/<int:review_id>/', views.edit_review, name='edit_perfume_review'),
   path('perfumes/<slug:slug>/delete_review/<int:review_id>/', views.delete_review, name='delete_perfume_review'),
    
   path('duplicates/<slug:slug>/edit_review/<int:review_id>/', views.edit_duplicate_review, name='edit_duplicate_review'),
   path('duplicates/<slug:slug>/delete_review/<int:review_id>/', views.delete_duplicate_review, name='delete_duplicate_review'),
]



# added urls to view home review_edit in views and review_delete
