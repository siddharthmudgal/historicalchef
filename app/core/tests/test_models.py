from django.test import TestCase
from .. import models


class TestEvent(TestCase):

    def test_event_model_creation(self):
        """this function tests if the event model creation"""
        event = models.Event.objects.create(
            created_at='1526123095',
            email='diego@chefhero.com',
            environment='production',
            component='orders',
            message='the buyer # 123456 has placed an order successfully',
            data_payload='{ "order_id": 123, "amount":300 }'
        )

        self.assertEqual(event.__str__(), 'diego@chefhero.com')
        self.assertNotEqual(event.__str__(), 'hellochef@chefhero.com')
        self.assertEqual(event.component, 'orders')
        self.assertNotEqual(event.component, 'orders123')
