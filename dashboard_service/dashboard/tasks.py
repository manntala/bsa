from celery import shared_task, current_task
from datetime import datetime
import requests
from django.db import transaction
from .models import MonthlyBooking, DailyBooking
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=5, default_retry_delay=10)
def fetch_and_update_bookings(self):
    try:
        response = requests.get(f"{settings.DATA_PROVIDER_URL}/events/")
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error fetching events: {e}")
        raise self.retry(exc=e)

    api_response = response.json()
    logger.info(f"API response: {api_response}")
    events = api_response.get('results', [])
    
    if not events:
        logger.info("No new events found. Exiting.")
        return

    logger.info(f"Fetched {len(events)} events.")

    for event in events:
        logger.info(f"Processing event: {event} (type: {type(event)})")
        try:
            if not isinstance(event, dict):
                logger.error(f"Unexpected event format: {event}")
                continue

            hotel_id = event.get('hotel_id')
            night_of_stay = event.get('night_of_stay')

            if hotel_id is None or night_of_stay is None:
                logger.error(f"Missing data in event: {event}")
                continue

            try:
                event_date = datetime.fromisoformat(night_of_stay).date()
            except ValueError as e:
                logger.error(f"Invalid date format for event {event}: {e}")
                continue

            with transaction.atomic():
                monthly_booking, created = MonthlyBooking.objects.get_or_create(
                    hotel_id=hotel_id,
                    year=event_date.year,
                    month=event_date.month,
                    defaults={'booking_count': 0}
                )
                monthly_booking.booking_count += 1
                monthly_booking.save()
                logger.info(f"MonthlyBooking updated for {hotel_id} in {event_date.year}-{event_date.month}.")

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
