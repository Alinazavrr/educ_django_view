# Generated by Django 4.2.2 on 2023-07-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('s', models.FloatField()),
                ('district', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
            ],
        ),
    ]