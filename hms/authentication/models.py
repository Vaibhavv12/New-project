from pyexpat import model
from django.db import models

# Create your models here.
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from numpy import product

# Create your models here.
class userTable(models.Model):
    id = models.AutoField
    user_id = models.CharField(max_length=30)
    is_student = models.BooleanField()
    is_verified = models.BooleanField()
    user_name =  models.CharField(max_length=45)
    user_address =  models.CharField(max_length=45)
    user_DOB = models.CharField(max_length=15)
    user_presentyear = models.CharField(max_length=15)
    user_LastSemScore = models.IntegerField()
    user_disability = models.CharField(max_length=3)
    user_sscmarks = models.IntegerField()
    user_hscmarks = models.IntegerField()
    user_cetscore = models.IntegerField()
    # userentry_dateTime = models.DateTimeField()
    user_gender = models.CharField(max_length=10)
    user_is_requested = models.CharField(max_length=10)
    user_hostel = models.CharField(max_length=10)
    user_room = models.CharField(max_length=10)
    # user_image = models.ImageField(upload_to='static/home/')

    def __str__(self):
        return self.entry_name    