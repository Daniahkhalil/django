# Generated by Django 4.0.3 on 2022-04-11 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('final_exam_app', '0005_alter_car_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='final_exam_app.user'),
        ),
    ]