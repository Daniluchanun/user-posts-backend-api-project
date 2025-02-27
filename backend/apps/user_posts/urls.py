from django.urls import path

from apps.user_posts.views import PostDetailView, PostListCreateView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post_list_create'),
    path('/<int:pk>', PostDetailView.as_view(), name='post_detail'),  
]
