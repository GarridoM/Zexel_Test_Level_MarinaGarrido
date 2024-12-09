from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.payment.models import Payment
from decimal import Decimal

class PaymentModelTest(TestCase):
    def setUp(self):
        self.valid_payment_data = {
            'source_amount': Decimal('100.00'),
            'source_currency': 'USD',
            'source_country': 'US',
            'target_amount': Decimal('85.00'),
            'target_currency': 'EUR',
            'target_country': 'DE',
            'status': 'pending',
            'concept': 'Test payment',
            'rate_exchange': Decimal('0.85'),
            'sender_full_name': 'John Doe',
            'receiver_full_name': 'Jane Smith'
        }

    def test_valid_payment_creation(self):
        payment = Payment.objects.create(**self.valid_payment_data)
        self.assertIsInstance(payment, Payment)

    def test_negative_amount_validation(self):
        invalid_data = self.valid_payment_data.copy()
        invalid_data['source_amount'] = Decimal('-100.00')
        with self.assertRaises(ValidationError):
            payment = Payment(**invalid_data)
            payment.full_clean()

    def test_invalid_country_code(self):
        invalid_data = self.valid_payment_data.copy()
        invalid_data['source_country'] = 'USA'  # Invalid ISO code
        with self.assertRaises(ValidationError):
            payment = Payment(**invalid_data)
            payment.full_clean()

    def test_invalid_currency_code(self):
        invalid_data = self.valid_payment_data.copy()
        invalid_data['source_currency'] = 'USDD'  # Invalid ISO code
        with self.assertRaises(ValidationError):
            payment = Payment(**invalid_data)
            payment.full_clean()

    def test_same_source_target_country(self):
        invalid_data = self.valid_payment_data.copy()
        invalid_data['target_country'] = 'US'  # Same as source_country
        with self.assertRaises(ValidationError):
            payment = Payment(**invalid_data)
            payment.full_clean()

    def test_valid_status_choices(self):
        for status, _ in Payment.STATUS_CHOICES:
            valid_data = self.valid_payment_data.copy()
            valid_data['status'] = status
            payment = Payment.objects.create(**valid_data)
            self.assertEqual(payment.status, status)

    def test_invalid_status_choice(self):
        invalid_data = self.valid_payment_data.copy()
        invalid_data['status'] = 'invalid_status'
        with self.assertRaises(ValidationError):
            payment = Payment(**invalid_data)
            payment.full_clean()

    def test_rate_exchange_precision(self):
        valid_data = self.valid_payment_data.copy()
        valid_data['rate_exchange'] = Decimal('0.8523')
        payment = Payment.objects.create(**valid_data)
        self.assertEqual(payment.rate_exchange, Decimal('0.8523'))

    def test_max_length_fields(self):
        long_name = 'A' * 256
        invalid_data = self.valid_payment_data.copy()
        invalid_data['sender_full_name'] = long_name
        with self.assertRaises(ValidationError):
            payment = Payment(**invalid_data)
            payment.full_clean()

    def test_concept_optional(self):
        valid_data = self.valid_payment_data.copy()
        valid_data.pop('concept')
        payment = Payment.objects.create(**valid_data)
        self.assertIsNone(payment.concept)

    def test_default_status(self):
        valid_data = self.valid_payment_data.copy()
        valid_data.pop('status')
        payment = Payment.objects.create(**valid_data)
        self.assertEqual(payment.status, 'Draft')
