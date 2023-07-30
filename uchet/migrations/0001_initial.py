# Generated by Django 4.1.7 on 2023-03-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField()),
                ('work_hours', models.TimeField()),
                ('date_purch', models.DateField()),
                ('guarant', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_purch', models.DateField()),
                ('acc', models.SmallIntegerField()),
                ('work_hours', models.TimeField()),
                ('number', models.SmallIntegerField()),
                ('guarant', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='journ_bat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('work_hours', models.TimeField()),
                ('number', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_purch', models.DateField()),
                ('acc', models.SmallIntegerField()),
                ('work_hours', models.TimeField()),
                ('malf', models.CharField(max_length=30)),
                ('date_rep', models.DateField()),
            ],
        ),
    ]
