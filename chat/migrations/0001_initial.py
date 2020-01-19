# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=20)),
                ('comp_name', models.CharField(max_length=50)),
                ('exp', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('option_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileQuestionMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order', models.IntegerField()),
                ('should_display', models.BooleanField()),
                ('is_required', models.BooleanField()),
                ('default', models.CharField(max_length=200, blank=True, null=True)),
                ('profile_id', models.ForeignKey(to='chat.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.IntegerField(primary_key=True, serialize=False)),
                ('QuestionName', models.CharField(max_length=200)),
                ('parameter', models.CharField(max_length=40)),
                ('type', models.IntegerField()),
                ('profile', models.ManyToManyField(to='chat.Profile', through='chat.ProfileQuestionMapping')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('job_id', models.ForeignKey(to='chat.Job')),
            ],
        ),
        migrations.AddField(
            model_name='profilequestionmapping',
            name='question',
            field=models.ForeignKey(to='chat.Question'),
        ),
        migrations.AddField(
            model_name='option',
            name='question_id',
            field=models.ForeignKey(on_delete=True, to='chat.Question'),
        ),
        migrations.AddField(
            model_name='job',
            name='profile',
            field=models.ForeignKey(to='chat.Profile'),
        ),
    ]
