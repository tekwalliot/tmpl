# Generated by Django 3.2.8 on 2021-12-24 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swpsdata', '0026_alter_donations_receipt_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='Issued_By',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swpsdata.staff'),
        ),
        migrations.AlterField(
            model_name='donations',
            name='Receipt_No',
            field=models.CharField(blank=True, help_text='Receipt Number', max_length=10, null=True, unique=True),
        ),
    ]