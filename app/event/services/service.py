# all business logics related to events module can be found here
import time
from datetime import datetime

import django
from django.http import Http404

from core.models import Event


def is_key_valid(data, key):
    """helper function to verify presence of key"""
    if data.__contains__(key):
        if data[key] is not None:
            if len(data[key]) != 0:
                return True
    return False


def selectively_find_events(eventSearch):
    """this implements the find functionality
    using the data received in the request"""
    event_filter = Event.objects

    if eventSearch is None or len(eventSearch) == 0:
        raise Http404

    if is_key_valid(eventSearch, 'email') is True:
        event_filter = event_filter.filter(email=eventSearch['email'])

    if is_key_valid(eventSearch, 'environment') is True:
        event_filter = event_filter.filter(
            environment=eventSearch['environment'])

    if is_key_valid(eventSearch, 'component') is True:
        event_filter = event_filter.filter(
            component=eventSearch['component'])

    if is_key_valid(eventSearch, 'message') is True:
        event_filter = event_filter.filter(
            message__icontains=eventSearch['message'])

    if is_key_valid(eventSearch, 'created_at') is True:
        dt = eventSearch['created_at']
        ts = time.mktime(datetime.strptime(dt, '%d-%m-%Y').timetuple())
        upperts = ts + 86399
        event_filter = event_filter.filter(
            created_at__gte=int(ts), created_at__lte=int(upperts)
        )

    if type(event_filter) == django.db.models.manager.Manager:
        raise Http404

    return event_filter
