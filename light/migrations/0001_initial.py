# Generated by Django 5.1.3 on 2024-12-03 16:24

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('action_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('on', 'On'), ('off', 'Off')], default='off', max_length=5)),
                ('place', models.CharField(max_length=255)),
                ('home', models.ForeignKey(help_text="The home associated with this door's status", on_delete=django.db.models.deletion.CASCADE, related_name='lights', to='home.home')),
            ],
        ),
    ]
