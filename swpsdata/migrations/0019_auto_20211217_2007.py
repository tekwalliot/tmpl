# Generated by Django 3.2.8 on 2021-12-17 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0018_alter_userrequest_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='Request_From',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swpsdata.account'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='Status',
            field=models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Not Accepted', 'Not Accepted')], max_length=20, null=True),
        ),
    ]
