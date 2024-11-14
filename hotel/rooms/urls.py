import include
from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'hotels', HotelListViewSet, basename='hotel-list'),
router.register(r'hotel-detail', HotelDetailViewSet, basename='hotel-detail')
router.register(r'users', UserProfileViewSet, basename='user-list')
router.register(r'booking', BookingViewSet, basename='book-list')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls))
    ]

