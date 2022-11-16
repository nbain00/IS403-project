from django.db import models

# Create your models here.

class Type(models.Model) :
    type = models.CharField(max_length=30)

    def __str__(self) :
        return (self.type)

class Restaurant(models.Model) :
    restaurant_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_code = models.BigIntegerField()
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    website = models.CharField(max_length=100)

    def __str__(self) :
        return (self.restaurant_name)

class Reviewer(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self) :
        return (self.first_name + ' ' + self.last_name)
class Review(models.Model) :
    reviewer = models.ForeignKey(Reviewer, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    rating = models.SmallIntegerField()
    notes = models.CharField(max_length=100)
