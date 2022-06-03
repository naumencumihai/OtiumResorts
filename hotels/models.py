from ast import Delete
from tabnanny import check
from django.db import models
from django.forms import CharField

# Create your models here.
class Hotel(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Room(models.Model):
    def __str__(self):
        return '{type} room {number} in {hotel}'.format(
            type = self.get_type_display(),
            number = self.number,
            hotel = self.hotel
        )  
    ROOM_TYPES = (
        ('S', 'Single'),
        ('D', 'Double'),
        ('T', 'Triple'),
        ('A', 'Apartment')
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    price = models.IntegerField()
    number = models.IntegerField()
    floor = models.IntegerField()
    type = models.CharField(max_length=1, choices=ROOM_TYPES)

class Booking(models.Model):
    def __str__(self):
        return 'Booking for {room} from {checkin} to {checkout}'.format(
            room = self.room,
            checkin = self.check_in_date,
            checkout = self.check_out_date
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    #associated with a user
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    
