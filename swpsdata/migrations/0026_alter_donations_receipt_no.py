# Generated by Django 3.2.8 on 2021-12-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0025_alter_donations_receipt_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='Receipt_No',
            field=models.CharField(blank=True, default=0, help_text='Receipt Number', max_length=10, null=True, unique=True),
        ),
    ]
