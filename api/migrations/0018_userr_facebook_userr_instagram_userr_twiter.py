# Generated by Django 4.1.3 on 2022-12-23 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_bids_chainid"),
    ]

    operations = [
        migrations.AddField(
            model_name="userr",
            name="facebook",
            field=models.CharField(default="facebook.com", max_length=255),
        ),
        migrations.AddField(
            model_name="userr",
            name="instagram",
            field=models.CharField(default="instagram.com", max_length=255),
        ),
        migrations.AddField(
            model_name="userr",
            name="twiter",
            field=models.CharField(default="twitter.com", max_length=255),
        ),
    ]