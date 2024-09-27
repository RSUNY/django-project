from django.urls import path
from . import views
from django.shortcuts import render
from django.http import HttpResponse
urlpatterns = [
    
   path('', views.PerfumesList.as_view(), name='Perfumes'),
   path('', views.DuplicateList.as_view(), name='Duplicates')
]
# added urls to view home review_edit in views and review_delete