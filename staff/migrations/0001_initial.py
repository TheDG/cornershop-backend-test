# Generated by Django 2.2.3 on 2019-07-25 02:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lunch_poll', '0002_delete_selection'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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