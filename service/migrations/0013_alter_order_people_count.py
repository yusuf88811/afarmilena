# Generated by Django 4.0.6 on 2022-07-16 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_alter_weddinghall_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='people_count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
