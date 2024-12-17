# Generated by Django 5.1.2 on 2024-12-17 00:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_rename_pens_profile_pinned_items"),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pen",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pens",
                to="accounts.profile",
            ),
        ),
    ]
