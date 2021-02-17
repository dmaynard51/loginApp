from django.db import models
from django.contrib.auth.models import User
from project1 import settings

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class invoices(models.Model):
    customer_number = models.CharField(default='', max_length=256)
    customer_name = models.CharField(default='', max_length=256)
    invoice_number = models.CharField(default='', max_length=256)
    invoice_date = models.CharField(max_length=256,default='')
    due_date = models.CharField(max_length=256,default='')
    salesOrder_number = models.CharField(max_length=256,default=0)
    amount_due = models.IntegerField(default=0)
    current_balance = models.IntegerField(default=0)
    past_due_1_30 = models.IntegerField(default=0)
    past_due_31_60 = models.IntegerField(default=0)
    over_90 = models.IntegerField(default=0)
    jde_customer_number = models.CharField(max_length=256,default='')
    business_unit = models.CharField(max_length=256,default='')
    rep = models.CharField(max_length=256,default='')
    netdays = models.CharField(max_length=256,default='')
    custType = models.CharField(max_length=256,default='')
    custCode = models.CharField(max_length=256,default='')
    custGroup3 = models.CharField(max_length=256,default='')
    custPO = models.CharField(max_length=256,default='')
