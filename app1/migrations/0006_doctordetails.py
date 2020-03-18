# Generated by Django 2.2.1 on 2020-03-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200316_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='doctor_pics')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('op', models.CharField(max_length=20)),
                ('blood', models.CharField(max_length=10)),
                ('mob', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
