# Generated by Django 3.2.8 on 2021-12-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Total_Hours',
            field=models.FloatField(max_length=5, null=True),
        ),
    ]
