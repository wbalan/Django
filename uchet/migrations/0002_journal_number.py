# Generated by Django 4.1.7 on 2023-03-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uchet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='number',
            field=models.SmallIntegerField(default=None),
        ),
    ]
