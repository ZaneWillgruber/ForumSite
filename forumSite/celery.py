from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forumSite.settings')

app = Celery('forumSite')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

app.conf.beat_schedule= {
        'add-every-30-sec' :{
            'task' : 'send_notif',
            'schedule' : crontab(minute='*/1')
            }
        }

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
