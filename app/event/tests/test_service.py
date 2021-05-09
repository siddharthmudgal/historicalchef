from django.test import TestCase

from core.models import Event
from ..services import service as service


def create_event(email='diego@chefhero.com',
                 created_at=1620551815,
                 environment='production',
                 component='orders',
                 message='the buyer # 123456 has placed an order successfully',
                 data_payload='{ "order_id": 123, "amount":300 }'):
    """helper function to create event"""
    Event.objects.create(
        email=email,
        created_at=created_at,
        environment=environment,
        component=component,
        message=message,
        data_payload=data_payload
    )


class Test(TestCase):
    def test_find_events_valid_email_based_search(self):
        """verify if the search for events works
        as expected"""
        create_event()
        create_event()
        create_event()
        create_event(email='hello@gmail.com')

        searchpayload = {
            'email': 'diego@chefhero.com'
        }
        data = service.selectively_find_events(searchpayload)
        self.assertEqual(len(data), 3)

    def test_find_events_invalid_email_based_search(self):
        """verify if the search for events works
        as expected"""
        searchpayload = {
            'email': 'diego_random@chefhero.com'
        }
        data = service.selectively_find_events(searchpayload)
        self.assertEqual(len(data), 0)

    def test_find_events_valid_environment_based_search(self):
        """verify if the search for events works
        as expected"""
        create_event()
        create_event()
        create_event()
        create_event(environment='different')

        searchpayload = {
            'environment': 'production'
        }
        data = service.selectively_find_events(searchpayload)
        self.assertEqual(len(data), 3)

    def test_find_events_invalid_environment_based_search(self):
        """verify if the search for events works
        as expected"""
        searchpayload = {
            'environment': 'production'
        }
        data = service.selectively_find_events(searchpayload)
        self.assertEqual(len(data), 0)

    def test_find_events_valid_component_based_search(self):
        """verify if the search for events works
        as expected"""
        create_event()
        create_event()
        create_event()
        create_event(component='different')

        searchpayload = {
            'component': 'orders'
        }
        data = service.selectively_find_events(searchpayload)
        self.assertEqual(len(data), 3)

    def test_find_events_invalid_component_based_search(self):
        """verify if the search for events works
        as expected"""
        searchpayload = {
            'component': 'orders123'
        }
        data = service.selectively_find_events(searchpayload)
        self.assertEqual(len(data), 0)

    def test_find_events_valid_message_based_search(self):
        """verify if the search for events works
        as expected"""
        create_event()
        create_event()
        create_event()
        create_event(message='different')

        searchpayload = {
            'message': 'placed'
        }
        data = service.selectively_find_events(searchpayload)
        self.assertEqual(len(data), 3)

    def test_find_events_invalid_message_based_search(self):
        """verify if the search for events works
        as expected"""
        searchpayload = {
            'message': 'placed'
        }
        data = service.selectively_find_events(searchpayload)
        self.assertEqual(len(data), 0)

    def test_find_events_valid_time_based_search(self):
        """verify if the search for events works
        as expected"""
        create_event()
        create_event()
        create_event()
        create_event(created_at=123456)

        searchpayload = {
            'created_at': '09-05-2021'
        }
        data = service.selectively_find_events(searchpayload)
        self.assertEqual(len(data), 3)

    def test_find_events_invalid_time_based_search(self):
        """verify if the search for events works
        as expected"""
        searchpayload = {
            'created_at': '09-05-2021'
        }
        data = service.selectively_find_events(searchpayload)
        self.assertEqual(len(data), 0)
