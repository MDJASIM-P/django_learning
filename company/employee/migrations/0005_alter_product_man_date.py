# Generated by Django 4.1.7 on 2023-05-12 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_product_man_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='man_date',
            field=models.DateField(verbose_name=datetime.date(2023, 5, 12)),
        ),
    ]
