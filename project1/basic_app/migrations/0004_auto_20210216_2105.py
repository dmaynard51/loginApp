# Generated by Django 3.1.5 on 2021-02-17 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20210215_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoices',
            name='invoiceDate',
        ),
        migrations.RemoveField(
            model_name='invoices',
            name='invoiceNumber',
        ),
        migrations.AddField(
            model_name='invoices',
            name='amount_due',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='business_unit',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='curren_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='custCode',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='custGroup3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='custPO',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='custType',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='customer_number',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='due_date',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='invoice_date',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='jde_customer_number',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='netdays',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='over_90',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='past_due_1_30',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='past_due_31_60',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='rep',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='salesOrder_number',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
