from django.db import models


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
