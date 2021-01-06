from django.db import models

# Create your models here.
class Plant(models.Model):
    """A plant the user has bought or wants to buy"""
    name = models.CharField(max_length=100)
    image_link = models.CharField(max_length=200)
    purchased = models.BooleanField()
    notes = models.TextField()

    def __str__(self):
        """Return string representation of plant name"""
        return self.name

