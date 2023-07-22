# Generated by Django 4.1.3 on 2023-07-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("networking", "0009_deposit_tx_hash"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="level_1",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="level_2",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="level_3",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="level_4",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="market_comission",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="personal_commision",
            field=models.FloatField(default=0),
        ),
    ]