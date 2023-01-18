import datetime
from django.db import models
import os

def get_filepath(request,filename):
    original_filename = filename
    timeNow =  datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow,original_filename)
    return os.path.join('uploads/',filename)

# Create your models here.

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
    name =models.CharField(max_length=100, null=True,blank=False)
    owner = models.CharField(max_length=100,null=True,blank=False)
    price = models.FloatField(max_length=10,null=True,blank=False)
    phone = models.CharField(max_length=10,null=True,blank=False)
    landmark = models.CharField(max_length=500,null=True,blank=False)
    description = models.TextField(max_length=500, null=True,blank=False)
    location = models.CharField(max_length=200, null=True, choices=LOCATION)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    image = models.ImageField(upload_to=get_filepath, null=True,blank=False)

    class Meta:
        db_table='SellProperty'

    def __str__(self):
        return self.name