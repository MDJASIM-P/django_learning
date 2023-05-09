# Generated by Django 4.1.7 on 2023-05-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_employee_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mng_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('qualification', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='profile_pics')),
            ],
            options={
                'db_table': 'Managers',
            },
        ),
    ]