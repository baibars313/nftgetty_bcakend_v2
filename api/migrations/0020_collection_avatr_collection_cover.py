# Generated by Django 4.1.3 on 2022-12-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0019_collection_alter_userr_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="collection",
            name="avatr",
            field=models.CharField(default="not", max_length=255),
        ),
        migrations.AddField(
            model_name="collection",
            name="cover",
            field=models.CharField(default="not", max_length=255),
        ),
    ]