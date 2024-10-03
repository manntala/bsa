from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MonthlyBooking, DailyBooking
from .serializers import MonthlyBookingSerializer, DailyBookingSerializer
from rest_framework.pagination import PageNumberPagination

class DashboardView(APIView):
    def get(self, request):
        daily_paginator = PageNumberPagination()
        daily_bookings = DailyBooking.objects.all()
        daily_data = daily_paginator.paginate_queryset(daily_bookings, request)
        serialized_daily_data = DailyBookingSerializer(daily_data, many=True)

        monthly_paginator = PageNumberPagination()
        monthly_bookings = MonthlyBooking.objects.all()
        monthly_data = monthly_paginator.paginate_queryset(monthly_bookings, request)
        serialized_monthly_data = MonthlyBookingSerializer(monthly_data, many=True)

        return Response({
            'daily_bookings': serialized_daily_data.data,
            'monthly_bookings': serialized_monthly_data.data,
            'daily_pagination': {
                'count': daily_bookings.count(),
                'next': daily_paginator.get_next_link(),
                'previous': daily_paginator.get_previous_link(),
            },
            'monthly_pagination': {
                'count': monthly_bookings.count(),
                'next': monthly_paginator.get_next_link(),
                'previous': monthly_paginator.get_previous_link(),
            },
        })
