# Generated by Django 3.2.8 on 2021-12-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0045_auto_20211229_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donations',
            name='Status',
        ),
        migrations.AlterField(
            model_name='donations',
            name='Paid_Through',
            field=models.CharField(choices=[('Paid-Cash', 'Paid-Cash'), ('Paid-Online', 'Paid-Online'), ('Due', 'Due')], max_length=20),
        ),
    ]
