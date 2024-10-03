from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateTimeFilter, NumberFilter
from .models import Event
from .serializers import EventSerializer
from celery import current_app
from rest_framework.pagination import PageNumberPagination
import logging

logger = logging.getLogger(__name__)

# Define a custom pagination class (optional)
class EventPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100 

class EventFilter(FilterSet):
    updated__gte = DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    updated__lte = DateTimeFilter(field_name="timestamp", lookup_expr='lte')
    night_of_stay__gte = NumberFilter(field_name="night_of_stay", lookup_expr='gte')
    night_of_stay__lte = NumberFilter(field_name="night_of_stay", lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['hotel_id', 'rpg_status', 'room_id', 'updated__gte', 'updated__lte', 'night_of_stay__gte', 'night_of_stay__lte']

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('timestamp')
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EventFilter
    ordering_fields = ['timestamp']
    ordering = ['timestamp']
    pagination_class = EventPagination

    def perform_create(self, serializer):
        instance = serializer.save()
        try:
            current_app.send_task('dashboard.tasks.fetch_and_update_bookings')
        except Exception as e:
            logger.error(f"Error sending task to Celery: {e}")
