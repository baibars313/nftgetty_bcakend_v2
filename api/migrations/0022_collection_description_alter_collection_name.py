# Generated by Django 4.1.3 on 2022-12-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0021_collection_contract"),
    ]

    operations = [
        migrations.AddField(
            model_name="collection",
            name="description",
            field=models.CharField(default="description", max_length=255),
        ),
        migrations.AlterField(
            model_name="collection",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
