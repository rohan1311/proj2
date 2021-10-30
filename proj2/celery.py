import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj2.settings')

app = Celery('proj2')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'every_minute' : {
        'task' : 'update_gainers',
        'schedule' : crontab(minute='*/5'),
    }
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
