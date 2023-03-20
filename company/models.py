from django.db import models


class Plans(models.Model):
    name = models.CharField(max_length=20)
    n_agent = models.IntegerField(default=5)
    n_leads = models.IntegerField(default=25)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Company(models.Model):
    name = models.CharField(max_length=50)
    plans = models.ForeignKey('company.Plans', null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    email = models.EmailField()

# Create your models here.
