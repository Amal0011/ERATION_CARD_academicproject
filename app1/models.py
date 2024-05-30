from django.db import models

# Create your models here.

class Shop_reg(models.Model):
    Sname = models.CharField(max_length=200)
    Panchayth = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200,unique=True)
    Ardno = models.CharField(max_length=200,unique=True)
    District = models.CharField(max_length=200)
    Cardcount = models.CharField(max_length=200)
    Username = models.CharField(max_length=200,unique=True)
    Password = models.CharField(max_length=200)
    Rating = models.CharField(max_length=200,default="0")
    Star1 = models.CharField(max_length=200,default="0")
    Star2 = models.CharField(max_length=200,default="0")
    Star3 = models.CharField(max_length=200,default="0")
    Star4 = models.CharField(max_length=200,default="0")


class Stock_table(models.Model):
    Card_type = models.CharField(max_length=200)
    Riceqt = models.CharField(max_length=200)
    Riceprc = models.CharField(max_length=200)
    Ricestck = models.CharField(max_length=200)
    Whtqt = models.CharField(max_length=200)
    Whtprc = models.CharField(max_length=200)
    Whtstck = models.CharField(max_length=200)
    Keroqt = models.CharField(max_length=200)
    Keroprc = models.CharField(max_length=200)
    Kerostck = models.CharField(max_length=200)
    Ataqt = models.CharField(max_length=200)
    Ataprc = models.CharField(max_length=200)
    Atastck = models.CharField(max_length=200)
    Month = models.CharField(max_length=200)
    Year = models.CharField(max_length=200,default="2022")


class Customer_reg(models.Model):
    Name = models.CharField(max_length=200)
    Cardno = models.CharField(max_length=200)
    Cardtype = models.CharField(max_length=200)
    No_fm = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200,unique=True)
    Address = models.CharField(max_length=200)
    Username = models.CharField(max_length=200,unique=True)
    Password = models.CharField(max_length=200)


class Purchase_table(models.Model):
    shopid=models.CharField(max_length=200,default="")
    shopname=models.CharField(max_length=200)
    usid=models.CharField(max_length=200)
    Riceqt=models.CharField(max_length=200)
    Riceprc=models.CharField(max_length=200)
    Whtqt=models.CharField(max_length=200)
    Whtprc=models.CharField(max_length=200)
    Keroqt=models.CharField(max_length=200)
    Keroprc=models.CharField(max_length=200)
    Ataqt=models.CharField(max_length=200)
    Ataprc=models.CharField(max_length=200)
    total=models.CharField(max_length=200)
    month=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    purchasecode=models.CharField(max_length=200)
    status=models.CharField(max_length=200,default="ordered")


