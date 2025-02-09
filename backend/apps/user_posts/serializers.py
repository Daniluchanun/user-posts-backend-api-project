from rest_framework import serializers

from apps.user_posts.models import PostModel


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = ('id', 'title', 'text', 'user', 'created_at', 'updated_at')

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "email": obj.user.email,
            "name": obj.user.profile.name,
        }

    def validate_title(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Назва поста не може бути порожньою.")
        if len(value) > 100:
            raise serializers.ValidationError("Назва поста не повинна перевищувати 100 символів.")
        return value


    def validate_text(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Текст поста не може бути порожнім.")
        return value