# Generated by Django 5.1.2 on 2025-01-19 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_profile_last_conversation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="last_conversation",
            field=models.ForeignKey(
                default="0",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.conversation",
            ),
        ),
    ]
