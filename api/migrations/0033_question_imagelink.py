# Generated by Django 4.1.3 on 2023-06-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0032_bidunlist_collection_collectionid_collection_onsale_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="imageLink",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
