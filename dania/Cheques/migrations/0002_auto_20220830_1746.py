# Generated by Django 2.2.4 on 2022-08-30 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cheques', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='billdate',
            field=models.DateTimeField(default=datetime.date(2022, 8, 30)),
        ),
        migrations.AlterField(
            model_name='cheque',
            name='chequedate',
            field=models.DateTimeField(default=datetime.date(2022, 8, 30)),
        ),
    ]