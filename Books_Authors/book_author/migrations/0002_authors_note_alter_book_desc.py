# Generated by Django 4.0.3 on 2022-04-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='note',
            field=models.TextField(default='notes'),
        ),
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(default='book description'),
        ),
    ]
