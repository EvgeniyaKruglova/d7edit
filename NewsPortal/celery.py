import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'action_every_20_seconds':{
        'task':'news.tasks.my_job',
        'schedule':20,
    },
}

# app.conf.beat_schedule = {
#     'action_every_30_seconds':{
#         'task':'news.tasks.send_notifications',
#         'schedule':30,
#     },
# }

# 'action_every_monday_8am': {
    #     'task': 'news.tasks.my_job',
    #     'schedule': crontab(hour=8, minute=0, day_of_week='monday'),