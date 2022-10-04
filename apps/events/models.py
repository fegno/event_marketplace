from django.db import models

# Create your models here.


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
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    linkedin_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()


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
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    vendor = models.ForeignKey('user.Vendor', on_delete=models.SET_NULL)
    event_type = models.CharField(choices=(
        (VIRTUAL, VIRTUAL),
        (HYBRID, HYBRID),
        (INPERSON, INPERSON)
    ), max_length=100, null=True, blank=True)
    venue = models.ForeignKey('Venue', on_delete=models.SET_NULL)


    def __str__(self):
        return self.name


class EventImages(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image