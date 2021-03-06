# Generated by Django 3.2.8 on 2021-12-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0029_expenses_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Is_Active',
            field=models.BooleanField(default=True, help_text='Unmark if Staff Resigned'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='User_Name',
            field=models.CharField(blank=True, help_text='User Name', max_length=20, null=True),
        ),
    ]
