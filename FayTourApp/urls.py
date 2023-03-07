from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('TourismPlace',viewTouristPlaces)
router.register('Hotel',viewHotel)
router.register('RateTourismPlace',viewTouristPlaces)
router.register('RateHotel',viewRateHotel)

urlpatterns = [
    path('', include(router.urls)),
]