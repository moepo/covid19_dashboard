# Generated by Django 3.0.5 on 2020-04-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_abr', models.CharField(max_length=3)),
                ('country', models.CharField(max_length=55)),
                ('region', models.CharField(max_length=10)),
                ('deaths', models.IntegerField()),
                ('cum_deaths', models.IntegerField()),
                ('confirmed', models.IntegerField()),
                ('cum_confirmed', models.IntegerField()),
            ],
        ),
    ]