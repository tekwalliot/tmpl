# Generated by Django 3.2.8 on 2021-12-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0039_auto_20211228_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='donations',
            name='Donor_Name',
            field=models.CharField(blank=True, help_text='Donor Name', max_length=100, null=True),
        ),
    ]