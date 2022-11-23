# Generated by Django 2.2.4 on 2022-08-29 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billame', models.CharField(max_length=45)),
                ('billdate', models.DateTimeField(default=datetime.date(2022, 8, 29))),
                ('billnumber', models.IntegerField()),
                ('billprice', models.FloatField()),
                ('billstatus', models.TextField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chequename', models.CharField(max_length=45)),
                ('chequedate', models.DateTimeField(default=datetime.date(2022, 8, 29))),
                ('returneddate', models.DateTimeField()),
                ('chequenumber', models.IntegerField()),
                ('chequeprice', models.FloatField()),
                ('chequestatus', models.TextField(max_length=45)),
                ('bankname', models.TextField(max_length=45)),
                ('branchname', models.TextField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]