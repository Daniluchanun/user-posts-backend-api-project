from django.db.models import Count

from django_filters import rest_framework as filters

from apps.user.models import UserModel


class UserFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name="id")
    email = filters.CharFilter(field_name="email", lookup_expr="icontains")
    name = filters.CharFilter(field_name="profile__name", lookup_expr="icontains")
    surname = filters.CharFilter(field_name="profile__surname", lookup_expr="icontains")
    age = filters.NumberFilter(field_name="profile__age")
    age_min = filters.NumberFilter(field_name="profile__age", lookup_expr="gte")
    age_max = filters.NumberFilter(field_name="profile__age", lookup_expr="lte")
    posts_count = filters.NumberFilter(method="filter_posts_count")

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'name', 'surname', 'age', 'age_min', 'age_max', 'posts_count']

    def filter_posts_count(self, queryset, name, value):
        return queryset.annotate(posts_count=Count('posts')).filter(posts_count=value)
