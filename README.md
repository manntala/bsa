This is incomplete!

1. cd in bsa_assessment
2. docker-compose up --build
3. docker exec -it dashboard_service python manage.py migrate (was not able to configure wait-for-it)
4. docker exec -it data_provider python manage.py migrate
5. docker network ls
6. and look for the network 'bsa_assessment_app_network'
7. docket network inspect bsa_assessment_app_network
8. copy the ip_address of data_provider normally would 172.18.0.4
9. use the ip_address in the DATA_PROVIDER_URL = http://172.18.0.4:8000
10. This should be updated in docker-compose.yml lines 54 and 72, dashboard_service/settings.py line 162 (then restart docker)
11. submit a Post data in localhost:8000/events/ and it will be updated in localhost:8001/dashboard/
12. I included a BaseCommand to send POST all data in data_provider:
13.  docker exec -it data_provider python manage.py post_events_csv --csv_file bsa_data.csv (Warning! This original bsa_data.csv has more than 65k rows)
14.  celery will automatically fetch the data from data_provider to dashboard_service
