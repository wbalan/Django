# Generated by Django 4.1.7 on 2023-03-20 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_routesheet_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='routesheet',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hello.card'),
        ),
        migrations.AlterField(
            model_name='routesheet',
            name='driver',
            field=models.CharField(default='ww', max_length=20, null=True),
        ),
    ]
