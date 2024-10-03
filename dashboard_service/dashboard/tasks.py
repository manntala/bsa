from celery import shared_task
from datetime import datetime
import requests
from django.db import transaction
from .models import MonthlyBooking, DailyBooking
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@shared_task
def fetch_and_update_bookings():
    while True:
        try:
            response = requests.get(f"{settings.DATA_PROVIDER_URL}/events/")
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Error fetching events: {e}")
            return
        
        events = response.json()
        
        if not events:
            logger.info("No new events found. Exiting fetch loop.")
            break  # Exit if no new events are found

        logger.info(f"Fetched {len(events)} events.")

        for event in events:
            logger.info(f"Processing event: {event}")
            try:
                hotel_id = event['hotel_id']
                event_date = datetime.fromisoformat(event['night_of_stay']).date()

                # Use atomic transaction for database updates
                with transaction.atomic():
                    # Update MonthlyBooking
                    monthly_booking, created = MonthlyBooking.objects.get_or_create(
                        hotel_id=hotel_id,
                        year=event_date.year,
                        month=event_date.month,
                        defaults={'booking_count': 0}
                    )
                    monthly_booking.booking_count += 1
                    monthly_booking.save()
                    logger.info(f"MonthlyBooking updated for {hotel_id} in {event_date.year}-{event_date.month}.")

                    # Update DailyBooking
                    daily_booking, created = DailyBooking.objects.get_or_create(
                        hotel_id=hotel_id,
                        date=event_date,
                        defaults={'booking_count': 0}
                    )
                    daily_booking.booking_count += 1
                    daily_booking.save()
                    logger.info(f"DailyBooking updated for {hotel_id} on {event_date}.")
            except Exception as e:
                logger.error(f"Error processing event {event}: {e}")

    logger.info("Finished processing all events.")
