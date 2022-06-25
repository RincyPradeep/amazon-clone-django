from django.urls import path
from api.v1.products import views
 
 
urlpatterns = [
    path('',views.products),
    path('gallery/',views.gallery),
    path('categories/',views.categories),
    path('banners/',views.banners),
    path('create-review-rate/',views.create_review_rate),
    path('get-review-rate/<int:pk>/',views.get_review_rate),

]
