# Generated by Django 2.1.7 on 2019-02-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20190227_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='confidence',
            field=models.FloatField(null=True),
        ),
    ]