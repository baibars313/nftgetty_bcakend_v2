# Generated by Django 4.1.3 on 2023-06-01 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0033_question_imagelink"),
    ]

    operations = [
        migrations.AddField(
            model_name="bidunlist",
            name="bidId",
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name="bidunlist",
            name="contract",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="bidunlist",
            name="tokenId",
            field=models.IntegerField(default=0),
        ),
    ]
