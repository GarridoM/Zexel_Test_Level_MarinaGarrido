import uuid
from django.db import models

class Payment(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Requested', 'Requested'),
        ('Approved', 'Approved'),
        ('Paid', 'Paid'),
        ('Deleted', 'Deleted'),
    ]

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    source_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    source_currency = models.CharField(max_length=20)
    source_country = models.CharField(max_length=20)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    target_currency = models.CharField(max_length=20)
    target_country = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')
    concept = models.CharField(max_length=255, null=True, blank=True)
    rate_exchange = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    sender_full_name = models.CharField(max_length=255, default='')
    receiver_full_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"{self.source_amount} {self.source_currency} to {self.target_amount} {self.target_currency}"
