# Generated by Django 4.1.7 on 2023-03-20 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_alter_routesheet_charge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routesheet',
            name='dateoperation',
        ),
    ]
