# Generated by Django 4.1.3 on 2023-07-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("networking", "0011_trade_disable"),
    ]

    operations = [
        migrations.AddField(
            model_name="netuser",
            name="wallet",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]