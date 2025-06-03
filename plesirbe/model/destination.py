from django.db import models


class Destination(models.Model):
    place_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    price = models.FloatField()
    hour = models.IntegerField()
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.place_name
