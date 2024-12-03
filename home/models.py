from django.db import models

import uuid

class Home(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    address = models.CharField(max_length=255, help_text="The address of the home")
    number_of_rooms = models.IntegerField(help_text="The total number of rooms in the home")
    has_garden = models.BooleanField(default=False, help_text="Indicates if the home has a garden")
    has_garage = models.BooleanField(default=False, help_text="Indicates if the home has a garage")
    owner_name = models.CharField(max_length=255, blank=True, help_text="The name of the home owner")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the home was added")

    def __str__(self):
        return f"Home at {self.address} - {self.number_of_rooms} rooms"
