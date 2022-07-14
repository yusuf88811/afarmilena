# Generated by Django 4.0.6 on 2022-07-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.PositiveIntegerField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='weddinghall',
            name='event',
            field=models.ManyToManyField(related_name='event_id', to='service.event'),
        ),
    ]
