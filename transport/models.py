from django.db import models

class TransportDetails(models.Model):
    stu_name=models.CharField(max_length=100)
    route=models.CharField(max_length=100)
    fees=models.PositiveIntegerField()
    
    def __str__(self):
        return TransportDetails
    class Meta:
        verbose_name="TransportDetails"
        verbose_name_plural="TransportDetails"

class RouteDetails(models.Model):
    route_name=models.CharField(max_length=100)
    distance=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    
    def __str__(self):
        return RouteDetails
    class Meta:
        verbose_name="RouteDetails"
        verbose_name_plural="RouteDetails"