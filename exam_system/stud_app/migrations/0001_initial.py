# Generated by Django 3.1.3 on 2020-11-02 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=6)),
                ('course_name', models.CharField(max_length=50)),
                ('course_desc', models.TextField(verbose_name='Course Description')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_code', models.CharField(max_length=3)),
                ('dept_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(default=0)),
                ('course_fk', models.ManyToManyField(to='stud_app.Course')),
                ('dept_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stud_app.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='dept_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stud_app.department'),
        ),
    ]