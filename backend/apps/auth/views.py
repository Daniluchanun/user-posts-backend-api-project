import secrets

from django.conf import settings

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            new_key = secrets.token_urlsafe(32)
            settings.SIMPLE_JWT["SIGNING_KEY"] = new_key

            return Response({"message": "Вихід успішний"}, status=200)
        except Exception as e:
            return Response({"error": "Невірний токен або помилка"}, status=400)
