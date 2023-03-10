# Generated by Django 4.1.7 on 2023-03-10 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_turf_turf_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('is_booked', models.BooleanField(default=True)),
                ('turf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.turf')),
            ],
        ),
    ]
