# Generated by Django 4.1.7 on 2023-04-12 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_turfuser'),
        ('manager', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.turfmanager'),
        ),
    ]