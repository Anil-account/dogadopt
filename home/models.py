from django.db import models
from django.core import validators
from django.contrib.auth.models import User



# Create your models here.
class Stories(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/uploads')
    details = models.TextField()
    date = models.DateField(auto_now_add=True)
    username = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    display = models.BooleanField(default=False)


class Adopt(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='static/uploads')
    description = models.TextField()
    age = models.IntegerField()
    sex = models.CharField(max_length=200, choices = GENDER, null=True)
    breed = models.CharField(max_length=100)
    postedby = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    postflag = models.BooleanField(default=False)






