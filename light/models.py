from django.db import models
from home.models import Home

import uuid

class Light(models.Model):
    STATUS_CHOICES = [
        ('on', 'On'),
        ('off', 'Off'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    action_at = models.DateTimeField()  # Field for storing date and time
    status = models.CharField(
        max_length=5,  # Maximum length of the choice value
        choices=STATUS_CHOICES,  # Restrict values to the choices defined
        default='off',  # Default value
    )
    place = models.CharField(max_length=255)
    home = models.ForeignKey(
        Home,  # The related model (Home)
        on_delete=models.CASCADE,  # Delete associated Dor when the related Home is deleted
        related_name='lights',  # Optional: To access all Dors from a Home instance, e.g., home.dors.all()
        help_text="The home associated with this door's status"
    )

    def __str__(self):
        return f"Light (status: {self.status}, action_at: {self.action_at})"
