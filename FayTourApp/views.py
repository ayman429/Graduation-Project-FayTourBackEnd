from django.shortcuts import render
from rest_framework import viewsets
from . models import *
from .serializers import *
from User.models import CustomUser

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django.db.models import Avg

class viewTouristPlaces(viewsets.ModelViewSet):
    search_fields = ['name','description','address','type']
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)

    ordering_fields = ['name', 'address','type']

    queryset = TouristPlaces.objects.all()
    serializer_class = TouristPlacesSerializer

    @action(detail=True, methods=['post'])
    def rate_TourismPlace(self, request, pk=None):
        if 'stars' in request.data:
            touristPlaces = TouristPlaces.objects.get(id=pk)
            stars = request.data['stars']
            username = request.data['username']
            user = CustomUser.objects.get(id=username)
            # update:
            try:
                rating = RateTouristPlaces.objects.get(user=username,touristPlaces=touristPlaces)
                rating.stars = stars
                rating.save()
                serializer = RateTouristPlacesSerializer(rating,many = False)
                json = {
                    'message': 'Tourism Place Rate Updated',
                    'result': serializer.data
                }
                return Response(json)
            # create:
            except:    
                rating = RateTouristPlaces.objects.create(user=user,touristPlaces=touristPlaces,stars=stars)
                serializer = RateTouristPlacesSerializer(rating,many = False)
                json = {
                    'message': 'Tourism Place Rate Created',
                    'result': serializer.data
                }
                return Response(json)
        return Response("json")
    
    @action(detail=False, methods=['Get'])
    def searchRateNamber(self, request):
        json = []
        json2 = []
        RateNamber = request.data['RateNamber']
        for obj in TouristPlaces.objects.all(): 
            if RateTouristPlaces.objects.filter(touristPlaces=obj).aggregate(Avg('stars'))['stars__avg'] == float(RateNamber):
                json.append(obj.id)
 
        for i in range(len(json)):
            TouristPlaces_by_rateNamber = TouristPlaces.objects.get(id = json[i])
            serializer = TouristPlacesSerializer(TouristPlaces_by_rateNamber)
            json2.append(serializer.data)
        return Response(json2) # , status=status.HTTP_200_OK

class viewHotel(viewsets.ModelViewSet):

    search_fields = ['name','description','address','City','Phone','TotalBeds']
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)

    ordering_fields = ['name', 'address']

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @action(detail=True, methods=['post'])
    def rate_Hotel(self, request, pk=None):
        if 'stars' in request.data:
            hotel = Hotel.objects.get(id=pk)
            stars = request.data['stars']
            username = request.data['username']
            user = CustomUser.objects.get(id=username)
            # update:
            try:
                rating = RateHotel.objects.get(user=username,hotel=hotel)
                rating.stars = stars
                rating.save()
                serializer = RateHotelSerializer(rating,many = False)
                json = {
                    'message': 'Hotel Rate Updated',
                    'result': serializer.data
                }
                return Response(json)
            # create:
            except:    
                rating = RateHotel.objects.create(user=user,hotel=hotel,stars=stars)
                serializer = RateHotelSerializer(rating,many = False)
                json = {
                    'message': 'Hotel Rate Created',
                    'result': serializer.data
                }
                return Response(json)
        return Response("json")
 
    @action(detail=False, methods=['Get'])
    def searchRateNamber(self, request):
        json = []
        json2 = []
        RateNamber = request.data['RateNamber']
        for obj in Hotel.objects.all(): 
            if RateHotel.objects.filter(hotel=obj).aggregate(Avg('stars'))['stars__avg'] == float(RateNamber):
                json.append(obj.id)
 
        for i in range(len(json)):
            hotels_by_rateNamber = Hotel.objects.get(id = json[i])
            serializer = HotelSerializer(hotels_by_rateNamber)
            json2.append(serializer.data)
        return Response(json2) # , status=status.HTTP_200_OK

class viewRateTouristPlaces(viewsets.ModelViewSet):
    queryset = RateTouristPlaces.objects.all()
    serializer_class = RateTouristPlacesSerializer

class viewRateHotel(viewsets.ModelViewSet):
    queryset = RateHotel.objects.all()
    serializer_class = RateHotelSerializer

