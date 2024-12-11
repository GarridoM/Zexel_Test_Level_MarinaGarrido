#!/bin/bash

# Make migrations for all apps
python manage.py makemigrations --settings=zexeltest.settings

# Apply database migrations
python manage.py migrate --settings=zexeltest.settings

# Collect static files
python manage.py collectstatic --noinput --settings=zexeltest.settings

# Create superuser
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@localhost.com').exists():
    User.objects.create_superuser(username='admin', email='admin@localhost.com', password='admin')
    print("Superuser created")
else:
    print("Superuser already exists")
EOF

# Create test data
python manage.py shell << EOF
import random
from django.contrib.auth import get_user_model
from apps.payment.models import Payment
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

# Define countries and currencies as lists
countries = [
    ("US", "United States"), ("GB", "United Kingdom"), ("DE", "Germany"),
    ("FR", "France"), ("JP", "Japan"), ("CA", "Canada"), ("AU", "Australia"),
    ("BR", "Brazil"), ("IN", "India"), ("CN", "China")
]

currencies = [
    ("USD", "US Dollar"), ("EUR", "Euro"), ("GBP", "British Pound"),
    ("JPY", "Japanese Yen"), ("CAD", "Canadian Dollar"), ("AUD", "Australian Dollar"),
    ("BRL", "Brazilian Real"), ("INR", "Indian Rupee"), ("CNY", "Chinese Yuan")
]

# Create random users
for i in range(20):
    username = f"user{i}"
    email = f"user{i}@example.com"
    User.objects.create_user(username=username, email=email, password="password123")

# Create random payments
names = [
    "John Smith", "Emma Johnson", "Michael Brown", "Olivia Davis", "William Wilson",
    "Sophia Martinez", "James Anderson", "Isabella Taylor", "Robert Thomas", "Ava Garcia",
    "David Rodriguez", "Mia Lopez", "Joseph Lee", "Charlotte Clark", "Daniel Walker",
    "Amelia Hall", "Christopher Allen", "Harper Young", "Matthew King", "Evelyn Scott"
]

for _ in range(50):
    sender_name = random.choice(names)
    receiver_name = random.choice(names)
    country = random.choice(countries)[0]
    currency = random.choice(currencies)[0]
    
    Payment.objects.create(
        source_amount=round(random.uniform(10, 1000), 2),
        source_currency=currency,
        source_country=country,
        target_amount=round(random.uniform(10, 1000), 2),
        target_currency=random.choice(currencies)[0],
        target_country=random.choice(countries)[0],
        status=random.choice(Payment.STATUS_CHOICES)[0],
        concept=f"Payment for order #{random.randint(1000, 9999)}",
        rate_exchange=round(random.uniform(0.5, 2), 6),
        sender_full_name=sender_name,
        receiver_full_name=receiver_name
    )

print("Test data created successfully")
EOF

# Start the main process
exec "$@"