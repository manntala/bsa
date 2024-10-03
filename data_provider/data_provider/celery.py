# # data_provider/celery.py

# from celery import Celery
# from celery.schedules import crontab

# app = Celery('data_provider')

# app.conf.beat_schedule = {
#     'load-csv-every-minute': {
#         'task': 'events.tasks.load_events_from_csv',
#         'schedule': crontab(minute='*'),  # Adjust as needed (e.g., every minute)
#     },
# }
