# Generated by Django 5.1.2 on 2025-01-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0012_remove_profile_following"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="following",
            field=models.ManyToManyField(related_name="followers", to="core.profile"),
        ),
    ]
