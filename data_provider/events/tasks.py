# import csv
# import os
# from celery import shared_task
# import requests
# from django.conf import settings
# import logging

# logger = logging.getLogger(__name__)

# @shared_task
# def load_events_from_csv():
#     csv_file_path = os.path.join(settings.BASE_DIR, 'bsa_data.csv')  # Adjust the path as needed

#     with open(csv_file_path, mode='r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             try:
#                 response = requests.post(
#                     f"{settings.DATA_PROVIDER_URL}/events/",
#                     json=row
#                 )
#                 response.raise_for_status()
#                 logger.info(f"Posted data: {row}")
#             except requests.RequestException as e:
#                 logger.error(f"Error posting data {row}: {e}")