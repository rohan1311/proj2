# Generated by Django 3.2.8 on 2021-10-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0004_auto_20211027_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gainer',
            name='turnover',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
