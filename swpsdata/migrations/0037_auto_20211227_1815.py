# Generated by Django 3.2.8 on 2021-12-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0036_alter_donations_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donations',
            name='Gothram',
        ),
        migrations.AlterField(
            model_name='donations',
            name='Date',
            field=models.DateField(null=True),
        ),
    ]
