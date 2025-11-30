from rest_framework import routers
from django.urls import path, include
from .views import ListingViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

