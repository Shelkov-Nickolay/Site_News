from django_filters import FilterSet, DateTimeFilter
from .models import News
from django.forms import DateTimeInput


class NewsFilter(FilterSet):
    addet_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )


    class Meta:
        model = News
        fields = {
            'name': ['icontains'],
            'categoryType': ['exact'],
        }
