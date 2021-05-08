from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from core.models import Event

EVENTS_URL = reverse('event:event-findevents')


def createEvent(email='diego@chefhero.com',
                environment='production',
                component='orders',
                message='the buyer # 123456 has placed an order successfully',
                data_payload='{ "order_id": 123, "amount":300,'
                            ' "created_at":123243 }'):

    """helper function to create event"""
    Event.objects.create(
        email=email,
        environment=environment,
        component=component,
        message=message,
        data_payload=data_payload
    )


class TestEventViewSet(TestCase):
    """verify event views"""

    def setUp(self):
        self.client = APIClient()

    def test_find_valid_query(self):
        """verify if status code 200 is returned
        for a valid query"""
        createEvent()
        searchpayload = {
            'email': 'diego@chefhero.com'
        }
        res = self.client.post(EVENTS_URL, searchpayload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_find_invalid_email(self):
        """verify if 404 is returned for resource
        not found"""

        searchpayload = {
            'email': 'diego123@chefhero.com'
        }
        res = self.client.post(EVENTS_URL, searchpayload)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
