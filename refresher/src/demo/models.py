from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):

    manufacturer_related = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
        default=None,
        null=True,
    )
    model_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    engine_capacity = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    transmission = models.CharField(max_length=20, null=True)
    mileage = models.PositiveIntegerField(default=0)
    num_seats = models.PositiveIntegerField(default=10)
    is_hybrid = models.BooleanField(default=False)
    is_electric = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model_name}"
