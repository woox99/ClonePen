# Generated by Django 5.1.2 on 2025-01-20 00:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_alter_pen_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="is_read",
            field=models.BooleanField(default=False),
        ),
    ]
