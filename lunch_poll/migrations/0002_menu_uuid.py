# Generated by Django 2.2.3 on 2019-07-24 19:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lunch_poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
