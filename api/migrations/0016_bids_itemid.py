# Generated by Django 4.1.3 on 2022-12-09 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_items_contract_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='itemId',
            field=models.IntegerField(default=0),
        ),
    ]
