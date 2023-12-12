from django.db import models

class Movement(models.Model):
    date = models.DateField()
    time = models.TimeField()
    moneda_from = models.CharField(max_length=100)
    cantidad_from = models.FloatField()
    moneda_to = models.CharField(max_length=100)
    cantidad_to = models.FloatField()