# Generated by Django 4.2 on 2024-10-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_id', models.IntegerField(db_index=True)),
                ('timestamp', models.DateTimeField(db_index=True)),
                ('rpg_status', models.IntegerField(choices=[(1, 'Booking'), (2, 'Cancellation')], db_index=True)),
                ('room_id', models.IntegerField(db_index=True)),
                ('night_of_stay', models.DateField(db_index=True)),
            ],
        ),
    ]
