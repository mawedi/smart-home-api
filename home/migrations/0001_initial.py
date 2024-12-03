# Generated by Django 5.1.3 on 2024-12-03 16:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('address', models.CharField(help_text='The address of the home', max_length=255)),
                ('number_of_rooms', models.IntegerField(help_text='The total number of rooms in the home')),
                ('has_garden', models.BooleanField(default=False, help_text='Indicates if the home has a garden')),
                ('has_garage', models.BooleanField(default=False, help_text='Indicates if the home has a garage')),
                ('owner_name', models.CharField(blank=True, help_text='The name of the home owner', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the home was added')),
            ],
        ),
    ]
