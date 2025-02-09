from rest_framework import generics, permissions

from apps.user_posts.filter import PostFilter
from apps.user_posts.models import PostModel
from apps.user_posts.serializers import PostSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
    permission_classes = [permissions.AllowAny]
    filterset_class = PostFilter


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PostModel.objects.filter(user=self.request.user)