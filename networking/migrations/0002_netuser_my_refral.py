# Generated by Django 4.1.3 on 2023-06-28 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("networking", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="netuser",
            name="my_refral",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]