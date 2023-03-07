from django.db import models
from User.models import CustomUser
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models import Avg
from django.core.validators import FileExtensionValidator
# Create your models here.

class TouristPlaces(models.Model):
    name = models.CharField(max_length=500,unique=True)
    type = models.CharField(max_length=500)
    description = models.TextField(default='')
    coordinatesX = models.FloatField() 
    coordinatesY = models.FloatField()
    address = models.CharField(max_length=100)
    originalImage = models.ImageField(upload_to='image')
    video = models.FileField(upload_to='video',validators=[FileExtensionValidator(allowed_extensions=["mp4"])])

    class Meta:
       unique_together = ("coordinatesX", "coordinatesY")

    def no_of_ratings(self):
        ratings = RateTouristPlaces.objects.filter(touristPlaces=self)
        return len(ratings)

    def avg_ratings(self):
        avg = RateTouristPlaces.objects.filter(touristPlaces=self).aggregate(Avg('stars'))['stars__avg']
        if avg is not None: return avg
        return 0
        
    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=500,unique=True)
    description = models.TextField(default='')
    originalImage = models.ImageField(upload_to='image')
    address = models.CharField(max_length=500)
    City = models.CharField(max_length=500)
    TotalBeds = models.IntegerField(default=0)
    Phone = models.CharField(max_length=500,unique=True)
    web = models.CharField(max_length=500,default='')
    email = models.EmailField(default='')
    Single = models.IntegerField(default=0)  
    Double = models.IntegerField(default=0)  
    Triple = models.IntegerField(default=0)   
    Sweet  = models.IntegerField(default=0)  
    chalet = models.IntegerField(default=0)  
    villa  = models.IntegerField(default=0)  

    def no_of_ratings(self):
        ratings = RateHotel.objects.filter(hotel=self)
        return len(ratings)

    def avg_ratings(self):
        avg = RateHotel.objects.filter(hotel=self).aggregate(Avg('stars'))['stars__avg']
        if avg is not None: return avg
        return 0
    
    def totalRooms(self):
        sum = self.Single+self.Double+self.Triple+self.Sweet+self.chalet+self.villa
        if sum !=0: return sum
        return 'unknown'

class HotelsImages(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(upload_to="image",blank=True,unique=True)   

class TourismImages(models.Model):
    touristPlaces = models.ForeignKey(TouristPlaces,on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(upload_to="image",blank=True,unique=True) 

class RateTouristPlaces(models.Model):
    touristPlaces = models.ForeignKey(TouristPlaces,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])


    class Meta:
        unique_together = (('user', 'touristPlaces'),)
        index_together = (('user', 'touristPlaces'),)

class RateHotel(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'hotel'),)
        index_together = (('user', 'hotel'),)



