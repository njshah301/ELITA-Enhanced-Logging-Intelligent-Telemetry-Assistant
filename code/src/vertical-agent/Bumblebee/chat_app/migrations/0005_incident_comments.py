# Generated by Django 5.1.7 on 2025-03-24 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0004_dashboard_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
