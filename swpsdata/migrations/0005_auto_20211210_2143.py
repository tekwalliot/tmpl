# Generated by Django 3.2.8 on 2021-12-10 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0004_salaries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month', models.DateField(unique=True)),
                ('Wrking_Days', models.FloatField(max_length=4, null=True)),
                ('Holidays', models.FloatField(max_length=4, null=True)),
                ('Extra_Working_Days', models.FloatField(blank=True, help_text='Extra Working Days If any', max_length=4, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Salaries',
            new_name='Monthatnd',
        ),
        migrations.CreateModel(
            name='Payslips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month', models.DateField(unique=True)),
                ('Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='swpsdata.account')),
            ],
        ),
    ]
