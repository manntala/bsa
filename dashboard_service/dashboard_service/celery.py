from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard_service.settings')

app = Celery('dashboard_service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['dashboard.tasks'])

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')