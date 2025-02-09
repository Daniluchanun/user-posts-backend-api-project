from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.user.filter import UserFilter
from apps.user.serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    """Відображає список користувачів та дозволяє створювати нових"""
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    def get_permissions(self):
        """Налаштування прав доступу: дозволяє створювати користувачів усім"""
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """Перегляд, оновлення або видалення користувача (тільки для себе)"""
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Отримує користувача тільки, якщо це він сам"""
        obj = get_object_or_404(UserModel, id=self.kwargs.get("pk"))
        if obj != self.request.user:
            self.permission_denied(self.request, message="Ви можете редагувати лише свій профіль.")
        return obj


class UserSearchByIdView(RetrieveAPIView):
    """Пошук користувача за ідентифікатором (ID)"""
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        return get_object_or_404(UserModel, id=self.kwargs.get("pk"))


class UserSearchByEmailView(ListAPIView):
    """Пошук користувачів за email (повний або частковий збіг)"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        email_query = self.kwargs.get("email", "")
        # Повертаємо всіх користувачів, чий email частково або повністю відповідає запиту
        return UserModel.objects.filter(email__icontains=email_query)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"detail": "Користувачів не знайдено."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
