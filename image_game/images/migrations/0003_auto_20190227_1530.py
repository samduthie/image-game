# Generated by Django 2.1.7 on 2019-02-27 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20190227_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='tags',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='images.Tag'),
        ),
    ]
