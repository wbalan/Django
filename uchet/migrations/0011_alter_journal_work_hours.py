# Generated by Django 4.1.7 on 2023-04-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uchet', '0010_alter_journal_work_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='work_hours',
            field=models.CharField(max_length=30),
        ),
    ]