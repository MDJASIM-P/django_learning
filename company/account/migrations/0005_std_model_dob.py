# Generated by Django 4.1.7 on 2023-05-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_std_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='std_model',
            name='DOB',
            field=models.DateField(db_column='Date of Birth', null=True),
        ),
    ]
