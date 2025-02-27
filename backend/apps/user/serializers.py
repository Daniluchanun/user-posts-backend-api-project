from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.user.models import UserProfileModel
from apps.user_posts.serializers import PostSerializer

UserModel = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    
    class Meta:
        model = UserProfileModel
        fields = ('id', 'name', 'surname', 'age', 'posts', 'created_at', 'updated_at')

    def get_posts(self, obj):
        return obj.user.posts.count()

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Ім’я повинно містити лише літери.")
        if len(value) > 25:
            raise serializers.ValidationError("Ім’я не повинно перевищувати 25 символів.")
        return value


    def validate_surname(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Прізвище повинно містити лише літери.")
        if len(value) > 25:
            raise serializers.ValidationError("Прізвище не повинно перевищувати 25 символів.")
        return value


    def validate_age(self, value):
        if value < 0 or value > 120:
            raise serializers.ValidationError("Вік повинен бути в діапазоні від 0 до 120 років.")
        return value


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'created_at', 'updated_at', 'profile')
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data:dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        UserProfileModel.objects.create(user=user, **profile)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if profile_data:
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()

        return instance