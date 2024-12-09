import json
from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from apps.payment.models import Payment

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)

class PaymentViewsTest(TestCase):
    def setUp(self):
        self.payment_data = {
            'source_amount': Decimal('100.00'),
            'source_currency': 'USD',
            'source_country': 'US',
            'target_currency': 'EUR',
            'target_country': 'DE',
            'target_amount': Decimal('85.00'),
            'rate_exchange': Decimal('0.85'),
            'concept': 'Test payment',
            'sender_full_name': 'John Doe',
            'receiver_full_name': 'Jane Smith'
        }

    def test_create_valid_payment(self):
        response = self.client.post(
            reverse('payment-list'),
            data=json.dumps(self.payment_data, cls=DecimalEncoder),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.json())

    def test_create_invalid_payment(self):
        invalid_data = self.payment_data.copy()
        invalid_data['source_amount'] = Decimal('-100.00')
        response = self.client.post(
            reverse('payment-list'),
            data=json.dumps(invalid_data, cls=DecimalEncoder),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('source_amount', response.json())

    def test_get_payment_list(self):
        # Create a few payments first
        for _ in range(3):
            Payment.objects.create(**self.payment_data)

        response = self.client.get(reverse('payment-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 3)

    def test_get_payment_detail(self):
        payment = Payment.objects.create(**self.payment_data)
        response = self.client.get(reverse('payment-detail', args=[payment.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['id'], str(payment.id))

    def test_update_payment(self):
        payment = Payment.objects.create(**self.payment_data)
        update_data = {'status': 'Paid'}
        response = self.client.patch(
            reverse('payment-detail', args=[payment.id]),
            data=json.dumps(update_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['status'], 'Paid')

    def test_delete_payment(self):
        payment = Payment.objects.create(**self.payment_data)
        response = self.client.delete(reverse('payment-detail', args=[payment.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify the payment is deleted
        get_response = self.client.get(reverse('payment-detail', args=[payment.id]))
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)