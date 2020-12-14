from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic a user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text



class Entry(models.Model):
    """Something specific learned about a topic"""
    # Don't allow connected topic deletion if this entry is deleted
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Django, please refer to multiples as entries not 'entrys'
    class Meta: 
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text) > 50: 
            return self.text[:50] +"..."
        else: 
            return self.text