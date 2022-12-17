from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

LOCATION_CHOICES = [
    ('TH', "Thrift"),
    ('ES', "Estate"),
    ('YS', "Yard Sale"),
    ('GW', "Goodwill"),
    ('MP', "Marketplace"),
    ('PR', "Private Sale"),
    ('OT', "Other")
]


class Expense(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    buyer = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='penner_expense')
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES, default="Thrift")
    amount = models.DecimalField()
    notes = models.TextField()
    purchased = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.name