# Generated by Django 4.1.1 on 2022-09-06 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_userr"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Proxies",
        ),
        migrations.DeleteModel(
            name="Userr",
        ),
    ]