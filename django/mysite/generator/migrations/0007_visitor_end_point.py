# Generated by Django 2.2.7 on 2021-12-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0006_auto_20211201_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='end_point',
            field=models.CharField(default=None, max_length=50),
        ),
    ]