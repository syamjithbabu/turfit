# Generated by Django 4.1.5 on 2023-05-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turfuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
