from distutils.command.upload import upload
from email.policy import default
from django.db import models
from numpy import product

# Create your models here.
class Entry(models.Model):
    entry_id = models.AutoField
    entry_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    entry_date = models.DateField()
    image = models.ImageField(upload_to="home/images",default="")

    def __str__(self):
        return self.entry_name    
 