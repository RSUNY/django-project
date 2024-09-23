from django.urls import path
from . import views


urlpatterns = [
    path('', views.ComparisonList.as_view(), name='home'),
]