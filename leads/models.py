from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Lead(models.Model):
    STATUS_CHOICES = (('New','New'),
                    ('Contacted','Contacted'),
                    ('Nurturing','Nurturing'),
                    ('Not Responding','Not Responding'),
                    ('Converted','Converted'),
    )
    SOURCE_CHOICES = (('Google','Google'),
                      ('Social','Social'),
                      ('Referral','Referral'),
                      ('Newsletter','Newsletter'),
                      )

    GENDER = (('Male','Male'),
              ('Female','Female'),)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER,max_length=20,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(choices=SOURCE_CHOICES,max_length=50)
    email = models.EmailField()
    dob = models.DateTimeField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=20, blank=True)
    agent = models.ForeignKey('agents.Agent',on_delete=models.SET_NULL,null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    company = models.ForeignKey('company.Company',null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{ self.fname } { self.lname }'

    @property
    def age(self) :
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
