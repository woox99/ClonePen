# Generated by Django 5.1.2 on 2024-12-17 00:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="pens",
            new_name="pinned_items",
        ),
    ]