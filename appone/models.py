from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class custreg(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=20)
    phoneno=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class venreg(models.Model):
    Company_Name=models.CharField(max_length=30)
    Company_id = models.CharField(max_length=20)
    Company_address = models.CharField(max_length=20)
    email = models.EmailField()
    lisence = models.FileField()
    phoneno = models.IntegerField()
    location=models.CharField(max_length=25)
    uname = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    status=models.CharField(max_length=20)
    def __str__(self):
        return self.Company_Name

class product(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    image=models.FileField()
    description=models.CharField(max_length=100)

class bookings(models.Model):
    location=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    phone_num=models.IntegerField()
    pin=models.IntegerField()
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=60)
    BR_no=models.IntegerField()
    Road_name=models.CharField(max_length=60)
    Alt_phno=models.IntegerField()
    Landmark=models.CharField(max_length=60)
    def __str__(self):
        return self.name

class vendor(models.Model):
    vendorname=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.FileField()

class Review(models.Model):
    user = models.ForeignKey(custreg, on_delete=models.CASCADE)
    Brand = models.CharField(max_length=40)
    review = models.TextField()
    def __str__(self):
        return self.review