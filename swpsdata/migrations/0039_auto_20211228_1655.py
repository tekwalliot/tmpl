# Generated by Django 2.2.1 on 2021-12-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0038_alter_donations_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Gothram', models.CharField(blank=True, max_length=255, null=True)),
                ('Address', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='donations',
            name='Gothram',
            field=models.CharField(blank=True, help_text='Donor Name', max_length=100, null=True),
        ),
    ]
