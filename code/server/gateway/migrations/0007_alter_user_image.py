# Generated by Django 4.2.6 on 2023-10-25 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0006_rename_otp_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.URLField(),
        ),
    ]
