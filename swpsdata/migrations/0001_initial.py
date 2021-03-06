# Generated by Django 3.2.8 on 2021-12-09 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Short_Name', models.CharField(max_length=15, null=True)),
                ('S_No', models.IntegerField(null=True, unique=True)),
                ('E_Id', models.CharField(blank=True, help_text='Employee ID', max_length=15, null=True, unique=True)),
                ('Designation', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('Working_As', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Join_Date', models.DateField()),
                ('Father_Name', models.CharField(max_length=50, null=True)),
                ('Adhaar_No', models.IntegerField(null=True, unique=True)),
                ('PAN_No', models.CharField(max_length=10, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Visitor_Name', models.CharField(max_length=30, null=True)),
                ('Address', models.TextField(blank=True, max_length=1000, null=True)),
                ('Time', models.DateTimeField(null=True)),
                ('End_Time', models.DateTimeField(null=True)),
                ('Total_Miniutes', models.IntegerField(null=True)),
                ('Visit_Category', models.CharField(choices=[('Staff', 'Staff'), ('Visitor', 'Visitor'), ('Friend', 'Friend'), ('Family', 'Family')], max_length=20)),
                ('Meeting_Points', models.TextField(blank=True, max_length=2000, null=True)),
                ('Visit_Review', models.CharField(choices=[('Useful', 'Useful'), ('Not Useful', 'Not Useful'), ('Productive', 'Productive'), ('Casual Meet', 'Casual Meet')], max_length=20)),
                ('Staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swpsdata.account')),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField(null=True)),
                ('Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='swpsdata.account')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Time', models.DateTimeField(null=True)),
                ('End_Time', models.DateTimeField(null=True)),
                ('Total_Hours', models.IntegerField(null=True)),
                ('Day_Status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave'), ('Half Day', 'Half Day'), ('Permission', 'Permission'), ('OD', 'OD'), ('Tour', 'Tour')], max_length=20, null=True)),
                ('Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='swpsdata.account')),
            ],
        ),
    ]
