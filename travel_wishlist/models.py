from django.db import models
from django.utils import timezone

# Create your models here.

class Place(models.Model):
	
	name = models.CharField(max_length=200)
	visited = models.BooleanField(default=False)
	date_visited = models.DateTimeField(max_length=200)
    notes = models.CharField(max_length=200)


    def __str__(self):
        return place = {self.name}, visited =  {self.visited}, 
               date_visited = {self.date_visited}, notes = {self.notes}
