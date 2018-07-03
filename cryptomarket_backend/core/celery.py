"""

For run celery use command: celery worker -A core -Q parser_tasks  -B -E -l error
Remove all tasks celery -A core purge

"""

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.vader')

app = Celery('cryptomarket_backend')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.timezone = 'UTC'

app.conf.task_queues = (
    Queue('parser_tasks', routing_key='parser.#'),
    Queue('vader', routing_key='vader.#'),
)

app.conf.beat_schedule = {
    'vader_scrappers': {
        'task': 'workers.tasks.vader_scrapper',
        'schedule': crontab(minute='00', hour='00'),
        'options': {'queue': 'vader'}
    }
}