# Generated by Django 4.1.4 on 2023-02-09 20:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('location', models.CharField(choices=[('TH', 'Thrift'), ('ES', 'Estate'), ('YS', 'Yard Sale'), ('GW', 'GW Online'), ('MP', 'Marketplace'), ('PR', 'Private Sale'), ('OT', 'Other')], default='Thrift', max_length=2)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('purchased', models.DateField(default=datetime.date.today)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='penner_expense', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
