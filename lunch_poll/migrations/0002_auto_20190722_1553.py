# Generated by Django 2.2.3 on 2019-07-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch_poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_date',
            field=models.DateField(unique=True),
        ),
    ]
