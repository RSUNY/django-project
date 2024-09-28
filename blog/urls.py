from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView, DetailView

# from the url accessed slug : uses the name, post_detail from the urlpattern and the slug variable 
urlpatterns = [
    path('', views.ComparisonList.as_view(), name='home'),
    path('<slug:slug>/', views.articles_detail.as_view(), name='articles_detail'),
    path('<slug:slug>/subs/<int:sub_id>', 
    views.subscription_list, name='subs'),
    path('<slug:slug>/notsubs/<int:sub_id>', 
    views.subscription_detail, name='notsubs'),
]

