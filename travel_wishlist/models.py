from django.db import models
from django.utils import timezone

# Create your models here.

class Place(models.Model):
	
	name = models.CharField(max_length=200)
	visited = models.BooleanField(default=False)
	date_visited = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(blank=True, null=True)

    def __str__(self):
        visit_time = timezone.visitedtime(self.date_visited, "%d %b %y")
        return '%s visited? %s %s %s' % (self.name, self.visited, visit_time, self.notes)
