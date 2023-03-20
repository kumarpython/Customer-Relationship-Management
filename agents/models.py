from django.db import models
from django.utils.datetime_safe import date

import company


class Agent(models.Model):
    GENDER = (('Male', 'Male'),
              ('Female', 'Female'),)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER, max_length=20, blank=True)
    email = models.EmailField()
    dob = models.DateTimeField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=20, blank=True)
    company = models.ForeignKey('company.Company', null=True, blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{ self.fname } { self.lname }'

    @property
    def age(self) :
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

# Create your models here.
