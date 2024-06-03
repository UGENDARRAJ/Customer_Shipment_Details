from django.db import models

class Shipment(models.Model):
    title = models.CharField(max_length=255)
    earliest_pickup_date = models.DateField()
    latest_pickup_date = models.DateField()
    earliest_delivery_date = models.DateField()
    latest_delivery_date = models.DateField()
    photo = models.ImageField(upload_to='shipment_photos/', blank=True, null=True)
    
    def __str__(self):
        return self.title
