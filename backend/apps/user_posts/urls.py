from django.urls import path

from apps.user_posts.views import PostCreateView, PostDetailView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('/create', PostCreateView.as_view(), name='post_create'),
    path('/<int:pk>', PostDetailView.as_view(), name='post_detail'),
]