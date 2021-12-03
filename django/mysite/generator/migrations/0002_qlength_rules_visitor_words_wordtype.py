# Generated by Django 2.2.7 on 2021-11-30 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QLength',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_len', models.IntegerField(default=5)),
                ('word_len', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_time', models.DateTimeField(verbose_name='Visit Time')),
            ],
        ),
        migrations.CreateModel(
            name='WordType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=200)),
                ('before', models.CharField(max_length=200)),
                ('after', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('word_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.WordType')),
            ],
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_type', models.CharField(max_length=50)),
                ('members', models.CharField(max_length=200)),
                ('word_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.WordType')),
            ],
        ),
    ]
