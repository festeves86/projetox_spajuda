# Generated by Django 3.0.5 on 2020-04-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuApp', '0010_list2'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='raio1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='list',
            name='raio2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='list',
            name='raio3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='list',
            name='raio4',
            field=models.BooleanField(default=False),
        ),
    ]
