# Generated by Django 5.1.2 on 2025-01-19 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_remove_profile_last_conversation"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="last_conversation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.conversation",
            ),
        ),
    ]