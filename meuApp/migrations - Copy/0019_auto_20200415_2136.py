# Generated by Django 3.0.5 on 2020-04-16 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuApp', '0018_auto_20200415_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='id',
        ),
        migrations.RemoveField(
            model_name='list2',
            name='id',
        ),
        migrations.AlterField(
            model_name='list',
            name='nro_whatsapp',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='list2',
            name='nro_whatsapp',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False),
        ),
    ]
