import datetime
from django.db import models
from django.contrib.auth.models import User
import os

def get_filepath(request,filename):
    original_filename = filename
    timeNow =  datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow,original_filename)
    return os.path.join('uploads/',filename)

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=12,null=True)
    Address = models.TextField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = "Customer"

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to=get_filepath, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table='category'

    def __str__(self):
        return self.name

    


class SellProperty(models.Model):
    CATEGORY = (
        ('Sale','Sale'),
        ('Rent','Rent'),
        ('Short Time','Short Time')
    )
    LOCATION = (
        ('Kerala','Kerala'),
        ('TamilNadu','TamilNadu'),
        ('Karnataka','Karnataka')
    )
    TYPE = (
        ('Land','Land'),
        ('House','House'),
        ('Villas','Villas'),
        ('PG','PG')
    )
    STATUS = (
        ('Approved','Approved'),
        ('Rejected','Rejected')
    )
    room=(("1","1"),("2","2"),("3","3"),("4","4"))
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    type = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    name =models.CharField(max_length=100, null=True,blank=False)
    owner = models.CharField(max_length=100,null=True,blank=False)
    price = models.CharField(max_length=10,null=True,blank=False)
    phone = models.CharField(max_length=10,null=True,blank=False)
    landmark = models.CharField(max_length=500,null=True,blank=False)
    description = models.TextField(max_length=500, null=True,blank=False)
    location = models.CharField(max_length=200, null=True, choices=LOCATION)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    image = models.ImageField(upload_to=get_filepath, null=True,blank=False)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    bed = models.CharField(max_length=3,null=True)
    baths = models.CharField(max_length=3,null=True)
    date_created = models.DateTimeField(auto_now_add=True,  null=True)


    class Meta:
        db_table='SellProperty'

    def __str__(self):
        return self.name
    


class Buyer(models.Model):
    property = models.ForeignKey(SellProperty, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=20, null=True)
    payment = models.CharField(max_length=5, null=True)
    dob = models.DateField(max_length=8, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        db_table='buyer'

    def __str__(self):
        return self.property.name


class EmiRequest(models.Model):
    YEAR=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    AMOUNT=(
        ('3000','3000'),
        ('4000','4000'),
        ('5000','5000'),
        ('6000','6000'),
        ('7000','7000'),
        ('8000','8000'),
        ('9000','9000'),
        ('10000','10000'),
         )
    property = models.ForeignKey(SellProperty,null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    dob = models.DateField(max_length=8,null=True)
    emiYear = models.CharField(max_length=2,null=True, choices=YEAR)
    emiAmount = models.CharField(max_length=5, null=True, choices=AMOUNT)
    bankName = models.CharField(max_length=100, null=True)
    bankBranch = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        db_table='emirequest'

    def __str__(self):
        return  self.property.name
    

