# Generated by Django 2.2.7 on 2021-12-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0005_visitor_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='visit_time',
        ),
        migrations.AddField(
            model_name='visitor',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
