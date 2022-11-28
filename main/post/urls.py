from django.db import router
from rest_framework import routers

from . import views
from django.urls import path, include

from .views import AllBlogAPIView, AllCommentsAPIView

urlpatterns = [
    path('', views.BlogView.as_view()),
    path("<slug:slug>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path('category/<slug:category_slug>/', views.BlogCategory.as_view(), name="post_category"),
    path('api/post', AllBlogAPIView.as_view({"get": "list", 'post': 'create'}), name="api_post"),
    path('api/post_detail/<str:post_slug>', AllBlogAPIView.as_view({"get": "retrieve", 'put': 'update'}), name="api_post_detail"),
    path('api/com', AllCommentsAPIView.as_view({"get": "list", 'post': 'create'}), name="api_com"),
]