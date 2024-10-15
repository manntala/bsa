1. cd in bsa_assessment
2. docker-compose up --build
3. submit a Post data in localhost:8100/events/ and it will be updated in localhost:8101/dashboard/
4. I included a BaseCommand to send POST all data in data_provider:
5.  docker exec -it data_provider python manage.py post_events_csv --csv_file bsa_data.csv (Warning! This original bsa_data.csv has more than 65k rows)
6.  celery will automatically fetch the data from data_provider to dashboard_service

UPDATED!!!
Fixed network config for docker-compose
Tested and working filters:
  localhost:8100/events?hotel_id=1
  localhost:8100/events?room_id=1
  etc...
  
