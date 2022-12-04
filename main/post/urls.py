from django.db import router
from rest_framework import routers

from . import views
from django.urls import path, include

from .views import AllBlogAPIView, AllCommentsAPIView, AddComment

urlpatterns = [
    path('', views.BlogView.as_view()),
    path('search/', views.Search.as_view(), name='search'),
    path("<slug:slug>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path('category/<slug:category_slug>/', views.BlogCategory.as_view(), name="post_category"),
    path('review/<int:pk>/', views.AddComment.as_view(), name="add_review"),
    path('api/post', AllBlogAPIView.as_view({"get": "list", 'post': 'create'}), name="api_post"),
    path('api/post/<str:post_slug>', AllBlogAPIView.as_view({"get": "retrieve", 'put': 'update'}),
         name="api_post_detail"),
    path('api/com', AllCommentsAPIView.as_view({"get": "list", 'post': 'create'}), name="api_com"),
    path('api/com/<int:pk>', AllCommentsAPIView.as_view({"get": "retrieve", 'put': 'update'}),
         name="api_com_detail"),
]
