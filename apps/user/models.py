from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.get_full_name()


class Attendee(User):
    pass


class Vendor(User):
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    linkedin_url = models.URLField()
    tax_name = models.CharField(max_length=50)
    tax_value = models.CharField(max_length=50)


