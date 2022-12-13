from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Restaurant(models.Model) :
    restaurant_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.BigIntegerField()
    type = models.CharField(max_length=30)
    website = models.CharField(max_length=100)

    def __str__(self) :
        return (self.restaurant_name)

class Reviewer(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self) :
        return (self.first_name + ' ' + self.last_name)
class Review(models.Model) :
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    notes = models.CharField(max_length=100)
