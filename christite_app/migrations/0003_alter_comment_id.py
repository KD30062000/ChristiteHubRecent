# Generated by Django 5.0.2 on 2024-02-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christite_app', '0002_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
