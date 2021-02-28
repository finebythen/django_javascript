from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class AlertModel(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AjaxCreate(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AjaxTable(models.Model):
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    age = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DropdownCar(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DropdownCarModel(models.Model):
    name = models.CharField(max_length=50)
    car = models.ForeignKey(DropdownCar, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DropdownOrder(models.Model):
    order_nr = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    description = models.CharField(max_length=50, null=False, blank=False, default="...")
    car = models.ForeignKey(DropdownCar, on_delete=models.CASCADE)
    model = models.ForeignKey(DropdownCarModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order: {self.order_nr}, of {self.model} by the company {self.car}"
