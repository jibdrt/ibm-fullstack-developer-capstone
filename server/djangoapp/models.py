# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    # Optional fields
    country = models.CharField(max_length=100, blank=True, null=True)
    founded_year = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    # Relationship: One Make -> Many Models
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")

    name = models.CharField(max_length=100)
    
    # Choices for car type
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    HATCHBACK = 'Hatchback'
    COUPE = 'Coupe'
    TRUCK = 'Truck'

    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (HATCHBACK, 'Hatchback'),
        (COUPE, 'Coupe'),
        (TRUCK, 'Truck'),
    ]

    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES, default=SEDAN)
    
    # Year field with validators
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )

    # Optional fields
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_added = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.name} ({self.car_make.name})"
