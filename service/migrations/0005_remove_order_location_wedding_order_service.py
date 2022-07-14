# Generated by Django 4.0.6 on 2022-07-13 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_order_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='location_wedding',
        ),
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ManyToManyField(related_name='order', to='service.service'),
        ),
    ]