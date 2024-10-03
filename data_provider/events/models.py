from django.db import models

class Event(models.Model):
    RPG_STATUS_CHOICES = (
        (1, 'Booking'),
        (2, 'Cancellation'),
    )

    hotel_id = models.IntegerField(db_index=True)
    timestamp = models.DateTimeField(db_index=True)
    rpg_status = models.IntegerField(choices=RPG_STATUS_CHOICES, db_index=True)
    room_id = models.IntegerField(db_index=True)
    night_of_stay = models.DateField(db_index=True)

    def __str__(self):
        return f"Event {self.id} - Hotel {self.hotel_id}"
