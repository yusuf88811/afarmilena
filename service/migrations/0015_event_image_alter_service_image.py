# Generated by Django 4.0.6 on 2022-07-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
