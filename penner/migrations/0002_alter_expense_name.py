# Generated by Django 4.1.4 on 2023-02-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Store Name'),
        ),
    ]
