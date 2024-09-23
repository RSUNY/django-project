from django.urls import path
from . import views

# from the url accessed slug : uses the name, post_detail from the urlpattern and the slug variable 
urlpatterns = [
    path('', views.ComparisonList.as_view(), name='home'),
    path('<slug:slug>/', views.blog_detail, name="blog_detai")
]

#path(
#     '<slug:slug>/delete_review/<int:slug_id>'
#     views.review_edit,
#     name='review_delete'
# )

