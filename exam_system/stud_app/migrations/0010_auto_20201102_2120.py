# Generated by Django 3.1.3 on 2020-11-02 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0009_auto_20201102_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='time_limit',
            field=models.DurationField(),
        ),
    ]
