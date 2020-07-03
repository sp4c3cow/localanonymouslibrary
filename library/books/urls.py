from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/', views.CreatePostView.as_view(), name='add-book'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
]