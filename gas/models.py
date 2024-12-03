from django.db import models
from home.models import Home

import uuid

class GasSensor(models.Model):
    GAS_TYPES = [
        ('CO', 'Carbon Monoxide'),
        ('CO2', 'Carbon Dioxide'),
        ('CH4', 'Methane'),
        ('O2', 'Oxygen'),
        ('VOC', 'Volatile Organic Compounds'),
    ]

    UNIT_CHOICES = [
        ('C', 'Celsius'),
        ('F', 'Fahrenheit'),
    ]

    CONCENTRATION_UNITS = [
        ('ppm', 'Parts Per Million'),
        ('ppb', 'Parts Per Billion'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    gas_type = models.CharField(
        max_length=10,
        choices=GAS_TYPES,
        default='CO',
        help_text="Type of gas being measured"
    )
    temperature = models.FloatField(
        help_text="Temperature in the environment"
    )
    unit = models.CharField(
        max_length=2,
        choices=UNIT_CHOICES,
        default='C',
        help_text="Unit of temperature"
    )
    gas_concentration = models.FloatField(
        help_text="Concentration of the gas"
    )
    concentration_unit = models.CharField(
        max_length=5,
        choices=CONCENTRATION_UNITS,
        default='ppm',
        help_text="Unit of gas concentration"
    )
    recorded_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the data was recorded"
    )
    home = models.ForeignKey(
        Home,  # The related model (Home)
        on_delete=models.CASCADE,  # Delete associated Dor when the related Home is deleted
        related_name='gas',  # Optional: To access all Dors from a Home instance, e.g., home.dors.all()
        help_text="The home associated with this door's status"
    )

    def __str__(self):
        return f"{self.gas_type} - {self.gas_concentration}{self.concentration_unit} at {self.temperature}{self.unit}"
