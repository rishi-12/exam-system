# Generated by Django 3.1.3 on 2020-11-03 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stud_app', '0018_auto_20201103_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dept_fk',
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
