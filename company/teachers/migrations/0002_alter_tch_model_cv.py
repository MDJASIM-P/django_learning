# Generated by Django 4.1.7 on 2023-05-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tch_model',
            name='cv',
            field=models.FileField(db_column='Resume', upload_to='tch_cvs/'),
        ),
    ]
