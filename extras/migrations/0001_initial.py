# Generated by Django 3.2.6 on 2021-08-19 14:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_from', models.CharField(max_length=30)),
                ('geo_to', models.CharField(max_length=30)),
                ('success', models.BooleanField(default=True)),
                ('search_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='searches', to='users.user')),
            ],
        ),
    ]
