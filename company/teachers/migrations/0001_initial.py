# Generated by Django 4.1.7 on 2023-05-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tch_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('std', models.IntegerField(verbose_name='standard')),
                ('div', models.CharField(choices=[('1', 'A'), ('2', 'B'), ('3', 'C')], max_length=100, verbose_name='division')),
                ('DOJ', models.DateField(help_text='dd/mm/yyyy', verbose_name='date of joining')),
                ('image', models.ImageField(upload_to='tch_pics/')),
                ('cv', models.FileField(upload_to='tch_cvs/')),
            ],
            options={
                'db_table': 'Teachers',
            },
        ),
    ]
