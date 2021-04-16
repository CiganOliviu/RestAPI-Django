from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    capital = models.CharField(max_length=100, default="")
    official_language= models.CharField(max_length=100, default="")
    currency = models.CharField(max_length=10, default="euro")


    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ExtremeSport(models.Model):
    name = models.CharField(max_length=100)
    period = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    coordinates = models.CharField(max_length=25)
    postal_code = models.CharField(max_length=15)
    regions = models.ForeignKey(Region, on_delete=models.CASCADE, default=1)
    sports = models.ManyToManyField(ExtremeSport)
    daily_costs = models.CharField(max_length=15, default="")

    class Meta:
        ordering = ['daily_costs']

    def __str__(self):
        return self.name












