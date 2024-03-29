# Generated by Django 4.1.3 on 2023-05-31 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0031_basefee_fee_collection_banned_userr_banned_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BidUnlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=255)),
                ("closed", models.BooleanField(default=False)),
                ("amount", models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name="collection",
            name="collectionId",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="collection",
            name="onsale",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="collection",
            name="price",
            field=models.IntegerField(default=1),
        ),
    ]
