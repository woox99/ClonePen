# Generated by Django 5.1.2 on 2025-01-19 21:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_alter_profile_last_conversation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="last_conversation",
        ),
    ]
