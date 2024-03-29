# Generated by Django 4.1.3 on 2023-07-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("networking", "0014_netuser_wallet"),
    ]

    operations = [
        migrations.CreateModel(
            name="Link",
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
                ("telegram", models.CharField(max_length=255)),
                ("facebook", models.CharField(max_length=255)),
                ("insta", models.CharField(max_length=255)),
                ("twitter", models.CharField(max_length=255)),
                ("youtube", models.CharField(max_length=255)),
            ],
        ),
    ]
