# Generated by Django 3.1.3 on 2020-11-02 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0003_question_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='qn_bank',
        ),
        migrations.AddField(
            model_name='question',
            name='course_fk',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='stud_app.course', verbose_name='Belongs to'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='Correct Answer'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_desc',
            field=models.TextField(max_length=100, verbose_name='Course Description'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qn_text',
            field=models.TextField(max_length=200, verbose_name='Question Description'),
        ),
        migrations.DeleteModel(
            name='QuestionBank',
        ),
    ]
