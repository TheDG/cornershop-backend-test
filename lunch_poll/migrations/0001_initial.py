# Generated by Django 2.2.3 on 2019-07-25 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lunch_poll.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_intro', models.CharField(max_length=200)),
                ('menu_date', models.DateField(unique=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('key', models.CharField(default=lunch_poll.models.generate_key, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField(verbose_name='Choice')),
                ('votes', models.IntegerField(default=0)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_options', to='lunch_poll.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customization', models.TextField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunch_poll.Menu')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunch_poll.Option')),
                ('selected_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='selection',
            constraint=models.UniqueConstraint(fields=('menu', 'selected_by'), name='just on selection per day'),
        ),
    ]
