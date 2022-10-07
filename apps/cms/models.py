from django.db import models

# this is dummy CMS app for clubbing with opther projects


class AbstractCMS(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='cms/')


    class Meta:
        abstract = True

    def __str__(self):
        return self.title



class AboutUs(models.Model):
    pass


class FAQ(models.Model):
    pass


class Testimonials(models.Model):
    pass


class Press(models.Model):
    pass


class Brochures(models.Model):
    pass


class OurTeam(models.Model):
    pass


class Career(models.Model):
    pass
