# Generated by Django 3.1.3 on 2020-11-02 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0007_auto_20201102_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='course_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stud_app.course', verbose_name='Course'),
        ),
    ]
