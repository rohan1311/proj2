# Generated by Django 3.2.8 on 2021-10-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0005_alter_gainer_turnover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
            ],
        ),
    ]
