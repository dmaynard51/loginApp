# Generated by Django 3.1.5 on 2021-02-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_invoices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='invoiceDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
