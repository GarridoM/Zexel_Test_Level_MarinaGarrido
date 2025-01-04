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
    source_currency = models.CharField(max_length=3) # Comentario 4: Los ISO de códigos de moneda no superan los 3 caracteres.
    source_country = models.CharField(max_length=3)  # Comentario 5: Los ISO de códigos de paises no superarn los 3 caracteres.
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    target_currency = models.CharField(max_length=3) # Comentario 6: Idem al comentario 4
    target_country = models.CharField(max_length=3) # Comentario 7: Idem al comentario 5
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Draft') # Comentario 8: Basándonos en los valores que hay en STATUS_CHOICE hemos reducido la longitud.
    concept = models.CharField(max_length=100, null=True, blank=True) # Comentario 9: El concepto (si nos basamos en entidades bancarias) no debe ser muy largo. Por ello, lo he reducido a 100, aunque lo reduciria aun más.
    rate_exchange = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    sender_full_name = models.CharField(max_length=100, default='') # Comentario 10: Pensando en nombres y apellidos completos, 255 es excesivo.
    receiver_full_name = models.CharField(max_length=100, default='') # Comentario 11: Idem al comentario 10.

    def __str__(self):
        return f"{self.source_amount} {self.source_currency} to {self.target_amount} {self.target_currency}"

    @staticmethod
    def get_valid_data():
        url = "https://countriesnow.space/api/v0.1/countries/currency"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()["data"]
                valid_iso_codes = [country["iso2"] for country in data]
                valid_currency_codes = [country["currency"] for country in data]
                return valid_iso_codes, valid_currency_codes
            else:
                raise ValidationError("Error: Not possible to check country and currency code", code=response.status_code)

        except requests.exceptions.RequestException as e:
            raise ValidationError("Error trying to connect with external API countriesnow: {e}")
    
    # COMENTARIO 1: En un principio pense en usar metodos separados para obtener la información teniendo en cuenta la API de countriesno. Dicho de otro modo,
    # me parecía más limpio. Sin embargo, me he dado cuenta que usando el endpoint especificado en is_valid_currency podemos obtener todos los datos que necesitamos.
    # Además, he refactorizado el código de modo que hacemos una funcion en la que obtenemos los datos necesarios y simplemente realizamos una comprobación. 
    # De ese modo, no realizamos un número elevado de llamadas (evitando que en un futuro nos bloqueen por protecciones de seguridad que tenga la propia API)
    # """Static method to validate country code (using https://countriesnow.space)"""
    # @staticmethod
    # def is_valid_country(country_code):
    #     url = "https://countriesnow.space/api/v0.1/countries/iso"
    #     try:
    #         response = requests.get(url)
    #         if response.status_code == 200:
    #             data = response.json()["data"]
    #             valid_iso_codes = [country["Iso2"] for country in data]
    #             return country_code in valid_iso_codes
    #         else:
    #             raise ValueError("Error: Not possible to check country code", code=response.status_code)

    #     except requests.exceptions.RequestException as e:
    #         raise ValueError("Error trying to connect with external API countriesnow: {e}")
    
    # """Static method to validate currency code (using https://countriesnow.space)"""
    # @staticmethod
    # def is_valid_currency(currency_code):
    #     url = "https://countriesnow.space/api/v0.1/countries/currency"
    #     try:
    #         response = requests.get(url)
    #         if response.status_code == 200:
    #             data = response.json()["data"]
    #             valid_currencies_codes = [country["currency"] for country in data]
    #             return currency_code in valid_currencies_codes
    #         else:
    #             raise ValueError("Error: Not possible to check currency", code=response.status_code)
    #     except requests.exceptions.RequestException as e:
    #         raise ValueError("Error trying to connect with external API countriesnow: {e}")

    """ Custom validations for Payment model"""
    def clean(self):
        # Validation: Monto should be positive
        if self.source_amount <= 0:
            raise ValidationError({"source_amount": "Source amount should be a positive value"}, code=406)
        if self.target_amount <= 0:
            raise ValidationError({"target_amount": "Target amount should be a positive value"}, code=406)
        
        valid_iso_codes, valid_currency_codes = self.get_valid_data()
        # Validation: Country codes
        if not self.source_country in valid_iso_codes:
            raise ValidationError({"source_country": "{self.source_country} is not a right country ISO code"}, code=406)
        if not self.target_country in valid_iso_codes:
            raise ValidationError({"target_country": "{self.target_country} is not a right country ISO code"}, code=406)
        
        # Validation: Currency codes
        if not self.source_currency in valid_currency_codes:
            raise ValidationError({"source_country": "{self.source_country} is not a right country ISO code"}, code=406)
        if not self.target_currency in valid_currency_codes:
            raise ValidationError({"target_country": "{self.target_country} is not a right country ISO code"}, code=406)
         
        
        # # COMENTARIO 2: (Comentario en RELACIÓN al COMENTARIO 1)Estas validaciones se realizarian si utilizaramos
        # las funciones previamente marcadas.

        # # Validation: Country codes
        # if not self.is_valid_country(self.source_country):
        #     raise ValidationError({"source_country": "{self.source_country} is not a right country ISO code"}, code=406)
        # if not self.is_valid_country(self.target_country):
        #     raise ValidationError({"target_country": "{self.target_country} is not a right country ISO code"}, code=406)
        
        # # Validation: Currency codes
        # if not self.is_valid_currency(self.source_currency): 
        #     raise ValidationError({"source_currency": "{self.source_currency} is not a right country ISO code"}, code=406)
        # if not self.is_valid_currency(self.target_currency):
        #     raise ValidationError({"target_currency": "{self.target_currency} is not a right country ISO code"}, code=406)

        # Validation: Origin Country and Destination Country should be different
        if self.source_country == self.target_country:
            raise ValidationError("Origin and Destination Country should be different", code=406)
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
