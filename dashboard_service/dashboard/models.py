from django.db import models

class MonthlyBooking(models.Model):
    hotel_id = models.IntegerField(db_index=True)
    year = models.IntegerField(db_index=True)
    month = models.IntegerField(db_index=True)
    booking_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('hotel_id', 'year', 'month')

    def __str__(self):
        return f"Hotel {self.hotel_id} - {self.year}-{self.month}: {self.booking_count}"

class DailyBooking(models.Model):
    hotel_id = models.IntegerField(db_index=True)
    date = models.DateField(db_index=True)
    booking_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('hotel_id', 'date')

    def __str__(self):
        return f"Hotel {self.hotel_id} - {self.date}: {self.booking_count}"
    
class LastFetch(models.Model):
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Last fetch timestamp: {self.timestamp}"

