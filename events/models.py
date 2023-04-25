from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    creator     = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name        = models.CharField(max_length=200)
    description = models.TextField()
    start_date  = models.DateField()
    final_date  = models.DateField()
    workload    = models.IntegerField()
    logo        = models.FileField(upload_to="logos")
    participant = models.ManyToManyField(User, related_name="event_participant", null=True)

    # color palette
    primary_color    = models.CharField(max_length=7)
    secondary_color  = models.CharField(max_length=7)
    background_color = models.CharField(max_length=7)

    def __str__(self) -> str:
        return self.name