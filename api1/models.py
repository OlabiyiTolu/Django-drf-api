from django.db import models

class Location(models.Model):
    locationName = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.locationName

class Item(models.Model):
    itemName = models.CharField(max_length=30)
    itemLocation = models.ForeignKey(Location, on_delete = models.CASCADE)
    dateAdded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.itemName