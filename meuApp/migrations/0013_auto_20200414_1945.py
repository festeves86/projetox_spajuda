# Generated by Django 3.0.5 on 2020-04-14 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuApp', '0012_auto_20200414_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='radio_dist1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='list',
            name='radio_dist2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='list',
            name='radio_dist3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='list',
            name='radio_dist4',
            field=models.BooleanField(default=False),
        ),
    ]
