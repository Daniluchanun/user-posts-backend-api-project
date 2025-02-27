from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.user_posts.filter import PostFilter
from apps.user_posts.models import PostModel
from apps.user_posts.permissions import IsOwnerOrReadOnly
from apps.user_posts.serializers import PostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]  # Читати можуть всі, створювати - тільки авторизовані
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return PostModel.objects.all()
