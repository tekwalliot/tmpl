# Generated by Django 3.2.8 on 2021-12-17 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0019_auto_20211217_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrequest',
            name='Request_Date',
        ),
    ]
