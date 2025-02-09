from django_filters import rest_framework as filters

from apps.user_posts.models import PostModel


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")  # Пошук по назві поста
    text = filters.CharFilter(field_name="text", lookup_expr="icontains")  # Пошук по тексту поста
    created_at = filters.DateTimeFilter(field_name="created_at")  # Фільтр за датою створення
    created_at_min = filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")  # Мінімальна дата створення
    created_at_max = filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")  # Максимальна дата створення
    updated_at = filters.DateTimeFilter(field_name="updated_at")  # Фільтр за датою оновлення
    updated_at_min = filters.DateTimeFilter(field_name="updated_at", lookup_expr="gte")  # Мінімальна дата оновлення
    updated_at_max = filters.DateTimeFilter(field_name="updated_at", lookup_expr="lte")  # Максимальна дата оновлення
    user_id = filters.NumberFilter(field_name="user__id")  # Фільтр за ID користувача
    user_email = filters.CharFilter(field_name="user__email", lookup_expr="icontains")  # Пошук за email користувача
    user_name = filters.CharFilter(field_name="user__profile__name", lookup_expr="icontains")  # Пошук за іменем користувача

    class Meta:
        model = PostModel
        fields = [
            'title', 'text', 'created_at', 'updated_at',
            'user_id', 'user_email', 'user_name'
        ]
