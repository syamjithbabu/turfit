# Generated by Django 4.2 on 2023-04-20 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turf',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.turfmanager'),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.turfmanager'),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='turf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.turf'),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='turf_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.turfuser'),
        ),
        migrations.AddField(
            model_name='category',
            name='turf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.turf'),
        ),
    ]
