from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from catalog.models import Product
from rewards.services import get_total_points

from .models import Order, OrderLineItem


class CheckoutTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='lee',
            email='lee@example.com',
            password='testpass123',
        )
        self.product = Product.objects.create(
            name='Strength Starter Plan',
            slug='strength-starter-plan',
            product_type=Product.WORKOUT_PLAN,
            description='A simple strength plan for new members.',
            price=19.99,
        )

    def test_checkout_creates_paid_order_and_purchase_reward(self):
        self.client.login(username='lee', password='testpass123')
        session = self.client.session
        session['bag'] = {str(self.product.id): 2}
        session.save()

        response = self.client.post(reverse('checkout'), {
            'full_name': 'Lee Carter',
            'email': 'lee@example.com',
            'phone_number': '07123456789',
            'street_address': '1 Test Street',
            'town_or_city': 'London',
            'postcode': 'SW1A 1AA',
            'country': 'United Kingdom',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderLineItem.objects.count(), 1)
        self.assertEqual(Order.objects.first().status, Order.PAID)
        self.assertEqual(get_total_points(self.user), 25)
