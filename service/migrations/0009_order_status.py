# Generated by Django 4.0.6 on 2022-07-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_alter_order_people_count_alter_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('In process', 'In process'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='In process', max_length=15),
        ),
    ]
