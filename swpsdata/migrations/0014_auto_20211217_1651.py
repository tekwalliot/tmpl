# Generated by Django 3.2.8 on 2021-12-17 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0013_auto_20211217_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='Request_From',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='Request_To',
            field=models.ForeignKey(limit_choices_to={'Department': 'Management'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='swpsdata.account'),
        ),
    ]
