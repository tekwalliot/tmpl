# Generated by Django 3.2.8 on 2021-12-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0032_alter_salaries_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='Paid_Through',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Online', 'Online')], max_length=20, null=True),
        ),
    ]
