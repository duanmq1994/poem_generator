# Generated by Django 2.2.7 on 2021-12-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0004_auto_20211201_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='ip',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
