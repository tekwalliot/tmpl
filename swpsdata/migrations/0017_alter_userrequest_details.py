# Generated by Django 3.2.8 on 2021-12-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0016_auto_20211217_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='Details',
            field=models.TextField(help_text='Add More Work/Visit Details or Add Personal Reasons if interested', max_length=1000, null=True),
        ),
    ]
