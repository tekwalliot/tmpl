# Generated by Django 3.2.8 on 2021-12-24 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0030_auto_20211224_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Join_Date',
            field=models.DateField(blank=True, help_text='Join Date', null=True),
        ),
    ]