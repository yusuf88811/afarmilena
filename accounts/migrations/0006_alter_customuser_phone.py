# Generated by Django 4.0.6 on 2022-07-15 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.PositiveIntegerField(blank=True, unique=True),
        ),
    ]