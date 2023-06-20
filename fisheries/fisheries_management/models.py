from django.db import models

# Create your models here.
class Marina(models.Model):
    Mid = models.AutoField(primary_key=True)
    Mname = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    class Meta:
        db_table = 'marina'

class Vehicle(models.Model):
    VId = models.AutoField(primary_key=True)
    VName = models.CharField(max_length=20)
    VOwner = models.CharField(max_length=30)
    Ownerphone = models.IntegerField(default=False)
    MId = models.ForeignKey(Marina, on_delete=models.CASCADE)
    Password = models.CharField(max_length=16)
    C_password = models.CharField(max_length=16)
    class Meta:
        db_table ='vehicle'

class Fishermen(models.Model):
    FId = models.AutoField(primary_key=True)
    FName = models.CharField(max_length=30)
    Address = models.CharField(max_length=20)
    Phonenumber = models.IntegerField(default=False)
    VId = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    class Meta:
        db_table = 'fishermen'

class Worksheet(models.Model):
    WId  = models.AutoField(primary_key=True)
    VId = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Fishspecie = models.CharField(max_length=20)
    quantity = models.IntegerField(default=False)
    Date = models.DateField()
    price = models.IntegerField(default=False)
    class Meta:
        db_table = 'worksheet'