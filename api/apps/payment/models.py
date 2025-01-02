import uuid
import requests
from django.core.exceptions import ValidationError
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

    """Static method to validate country code (using https://countriesnow.space)"""
    @staticmethod
    def is_valid_country(country_code):
        url = "https://countriesnow.space/api/v0.1/countries/iso"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()["data"]
                valid_iso_codes = [country["Iso2"] for country in data]
                return country_code in valid_iso_codes
            else:
                raise ValueError("Error: Not possible to check country code", code=response.status_code)

        except requests.exceptions.RequestException as e:
            raise ValueError("Error trying to connect with external API countriesnow: {e}")
    
    """Static method to validate currency code (using https://countriesnow.space)"""
    @staticmethod
    def is_valid_currency(currency_code):
        url = "https://countriesnow.space/api/v0.1/countries/currency"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()["data"]
                valid_currencies_codes = [country["currency"] for country in data]
                return currency_code in valid_currencies_codes
            else:
                raise ValueError("Error: Not possible to check currency", code=response.status_code)
        except requests.exceptions.RequestException as e:
            raise ValueError("Error trying to connect with external API countriesnow: {e}")

    """ Custom validations for Payment model"""
    def clean(self):
        # Validation: Monto should be positive
        if self.source_amount <= 0 or self.target_amount <= 0:
            raise ValidationError([
                ValidationError({"source_amount": "Monto should be a positive value"}, code=406),
                ValidationError({"target_amount": "Monto should be a positive value"}, code=406)
            ])
        
        # Validation: Country codes
        if not self.is_valid_country(self.source_country) or not self.is_valid_country(self.target_country):
            raise ValidationError([
                ValidationError({"source_country": "{self.source_country} is not a right country ISO code"}, code=406),
                ValidationError({"target_country": "{self.target_country} is not a right country ISO code"}, code=406)
            ])
        
        # Validation: Currency codes
        if not self.is_valid_currency(self.source_currency) or not self.is_valid_currency(self.target_currency):
            raise ValidationError([
                ValidationError({"source_currency": "{self.source_currency} is not a right country ISO code"}, code=406),
                ValidationError({"target_currency": "{self.target_currency} is not a right country ISO code"}, code=406)
            ])

        # Validation: Origin Country and Destination Country should be different
        if self.source_country == self.target_country:
            raise ValidationError("Origin and Destination Country should be different", code=406)
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
