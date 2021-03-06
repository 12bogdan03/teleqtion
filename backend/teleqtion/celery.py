from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teleqtion.settings.local')

app = Celery('teleqtion')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'collect_cryptocurrencies_rates': {
        'task': 'apps.payments.crypto_payments.tasks.collect_cryptocurrencies_rates',
        'schedule': 20.0,
    },
}
