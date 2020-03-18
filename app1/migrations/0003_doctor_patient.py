# Generated by Django 2.2.1 on 2020-03-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_Id', models.CharField(max_length=10)),
                ('birth_day', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('hospital', models.CharField(max_length=100)),
                ('Contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_day', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('Contact', models.IntegerField()),
            ],
        ),
    ]
