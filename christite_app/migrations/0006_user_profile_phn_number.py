# Generated by Django 5.0.3 on 2024-03-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christite_app', '0005_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='phn_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
