from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Data(models.Model):
    img = models.ImageField(upload_to='pics')


class Poster(models.Model):
    img = models.ImageField(upload_to='poster')


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    doctor_Id = models.CharField(max_length=10)
    birth_day = models.DateField(auto_now_add=False)
    gender = models.CharField(max_length=10)
    hospital = models.CharField(max_length=100)
    Contact = models.IntegerField()
    Im_doctor = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birth_day = models.DateField(auto_now_add=False)
    gender = models.CharField(max_length=10)
    Contact = models.IntegerField()

    def __str__(self):
        return self.name


class DoctorDetails(models.Model):
    img = models.ImageField(upload_to='doctor_pics')
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    op = models.CharField(max_length=20)
    blood = models.CharField(max_length=10)
    mob = models.IntegerField()
    description = models.CharField(max_length=1000)
    result=models.CharField(max_length=20)
    doctorname=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(blank=True,null=True,)
