# Generated by Django 3.1.5 on 2021-02-17 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_auto_20210216_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoices',
            old_name='curren_balance',
            new_name='current_balance',
        ),
    ]
