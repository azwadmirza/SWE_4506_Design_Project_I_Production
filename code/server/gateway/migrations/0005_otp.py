# Generated by Django 4.1.12 on 2023-10-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0004_remove_user_is_staff_user_image_user_verified_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('otp', models.CharField(max_length=6)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
