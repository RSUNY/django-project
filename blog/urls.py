from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

# from the url accessed slug : uses the name, post_detail from the urlpattern and the slug variable 
urlpatterns = [
    path('', views.ComparisonList.as_view(), name='home'),
    path("<int:subscribe_id>", views.articles_detail.as_view(), name='articles_detail'),
    path('<slug:slug>/', views.sub_detail.as_view, name='articles_list'),
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


#path(
#     '<slug:slug>/delete_review/<int:slug_id>'
#     views.review_edit,
#     name='review_delete'
# )
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

