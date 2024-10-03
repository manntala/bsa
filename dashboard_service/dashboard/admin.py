from django.contrib import admin
from .models import MonthlyBooking, DailyBooking, LastFetch

admin.site.register(MonthlyBooking)
admin.site.register(DailyBooking)
admin.site.register(LastFetch)
