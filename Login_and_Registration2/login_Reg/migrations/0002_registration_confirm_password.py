# Generated by Django 4.0.3 on 2022-04-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_Reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='confirm_password',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
    ]
