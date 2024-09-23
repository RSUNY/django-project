from django.urls import path
from . import views

urlpatterns = [
    
   path('', views.PerfumesList.as_view(), name='home'),
]
# added urls to view home review_edit in views and review_delete