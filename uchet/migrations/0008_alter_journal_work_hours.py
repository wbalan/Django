# Generated by Django 4.1.7 on 2023-04-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uchet', '0007_alter_journal_date_rep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='work_hours',
            field=models.FloatField(),
        ),
    ]
