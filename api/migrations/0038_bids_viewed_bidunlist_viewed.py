# Generated by Django 4.1.3 on 2023-06-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0037_bids_image_bids_link_bids_useraddress_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bids",
            name="viewed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="bidunlist",
            name="viewed",
            field=models.BooleanField(default=False),
        ),
    ]