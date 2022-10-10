from django.conf import settings
from django.db import models
from django.contrib.gis.db.models import PointField

# Create your models here.


class Location(models.Model):
    location = PointField(null=True, blank=True)
    # pincode = models.CharField(null=True, blank=True, validators=[pincode_required], max_length=8)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)


class Destination(models.Model):
    name = models.CharField(max_length=100)
    # location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Event(models.Model):
    VIRTUAL = 'Virtual'
    HYBRID = 'Hybrid'
    INPERSON = 'In-Person'


    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    price = models.FloatField()

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    vendor = models.ForeignKey('user.Vendor', on_delete=models.SET_NULL, related_name='events', blank=True, null=True)
    event_type = models.CharField(choices=(
        (VIRTUAL, VIRTUAL),
        (HYBRID, HYBRID),
        (INPERSON, INPERSON)
    ), max_length=100, default=INPERSON)
    venue = models.ForeignKey('Venue', on_delete=models.SET_NULL, related_name='events', null=True, blank=True)


    def __str__(self):
        return self.name


class EventImages(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image
