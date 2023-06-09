# Generated by Django 4.1.7 on 2023-06-02 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biotech', '0002_userprofile_question_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='answers_files/')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='questions_files/')),
            ],
        ),
        migrations.DeleteModel(
            name='Example',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='file',
        ),
        migrations.RemoveField(
            model_name='question',
            name='file',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='questionfile',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biotech.question'),
        ),
        migrations.AddField(
            model_name='answerfile',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biotech.answer'),
        ),
    ]
