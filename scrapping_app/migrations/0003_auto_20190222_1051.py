# Generated by Django 2.1.7 on 2019-02-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping_app', '0002_selectedorders_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedorders',
            name='price',
            field=models.IntegerField(),
        ),
    ]
