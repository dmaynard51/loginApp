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

    invoiceNumber = models.CharField(max_length=256)
    invoiceDate = models.DateField(blank=True, null=True)
