from basic_app.models import UserProfileInfo
from django.contrib import admin
from basic_app.models import invoices

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(invoices)