import csv
import os
import requests
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Post events from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--csv_file', 
            type=str, 
            default='bsa_data.csv', 
            help='Path to the CSV file. Default is bsa_data.csv in the current directory.'
        )

    def handle(self, *args, **options):
        csv_file_name = options['csv_file']
        csv_file_path = os.path.join(os.getcwd(), csv_file_name)

        if not os.path.exists(csv_file_path):
            self.stderr.write(self.style.ERROR(f"CSV file '{csv_file_name}' not found in the current directory."))
            return

        with open(csv_file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = {
                    'hotel_id': row['hotel_id'],
                    'timestamp': row['event_timestamp'],
                    'rpg_status': row['status'],
                    'room_id': row['room_reservation_id'],
                    'night_of_stay': row['night_of_stay']
                }

                try:
                    response = requests.post(
                        f"{settings.DATA_PROVIDER_URL}/events/",
                        json=data
                    )
                    response.raise_for_status()
                    self.stdout.write(self.style.SUCCESS(f"Successfully posted event: {data}"))
                except requests.exceptions.RequestException as e:
                    self.stderr.write(self.style.ERROR(f"Failed to post event {data}: {e}"))
