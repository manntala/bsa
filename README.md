This is incomplete!

1. cd in bsa_assessment
2. docker-compose up --build
3. docker network ls
4. and look for the network 'bsa_assessment_app_network'
5. docket network inspect bsa_assessment_app_network
6. copy the ip_address of data_provider normally would 172.19.0.4
7. use the ip_address in the DATA_PROVIDER_URL: http://172.19.0.4:8100
8. This should be updated in docker-compose.yml lines 54 and 72, dashboard_service/settings.py line 162 (then restart docker)
9. submit a Post data in localhost:8100/events/ and it will be updated in localhost:8101/dashboard/
10. I included a BaseCommand to send POST all data in data_provider:
11.  docker exec -it data_provider python manage.py post_events_csv --csv_file bsa_data.csv (Warning! This original bsa_data.csv has more than 65k rows)
12.  celery will automatically fetch the data from data_provider to dashboard_service
