# Generated by Django 4.1.3 on 2023-03-07 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0025_reward"),
    ]

    operations = [
        migrations.AddField(
            model_name="reward",
            name="rewardId",
            field=models.CharField(default=0, max_length=255),
        ),
    ]
