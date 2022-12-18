from django.db import models
from datetime import date
from django.contrib.auth.models import User

LOCATION_CHOICES = [
    ('TH', "Thrift"),
    ('ES', "Estate"),
    ('YS', "Yard Sale"),
    ('GW', "GW Online"),
    ('MP', "Marketplace"),
    ('PR', "Private Sale"),
    ('OT', "Other")
]


class Expense(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    buyer = models.ForeignKey(User, default='2',
                               on_delete=models.CASCADE,
                               related_name='penner_expense')
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES, default="Thrift")
    amount = models.DecimalField(decimal_places=2,max_digits=10)
    notes = models.TextField(blank=True, null=True)
    purchased = models.DateField(default=date.today)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.name