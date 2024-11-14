from django_filters import FilterSet
from .models import Hotel


class HotelFilterSet(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'hotel_name': ['exact'],
            'city': ['exact'],
            'stars': ['gt', 'lt'],
            'country': ['exact']
        }
