import django_filters
from django.contrib.auth.models import User
from django_filters import CharFilter


class UsernameFilter(django_filters.FilterSet):
    username = CharFilter(field_name='username',
    lookup_expr = 'icontains')

    class Meta:
        model = User
        fields = ''