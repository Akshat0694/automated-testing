# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-16 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_paper', models.FileField(blank=True, max_length=200, upload_to=b'/Users/akshat/Documents/Tand_Labs/automated_testing/media/Question_paper_%Y-%m-%d_%H:%M:%S.%f', verbose_name='Queestion paper')),
                ('num_of_ques', models.PositiveIntegerField(null=True, verbose_name='number of questions in the test')),
                ('allow_access', models.BooleanField(default=False, verbose_name='Allow Access')),
                ('created_by', models.CharField(blank=True, default='', max_length=1000, verbose_name='Create by')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='TestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_file', models.FileField(blank=True, max_length=200, upload_to=b'/Users/akshat/Documents/Tand_Labs/automated_testing/media/TestUser', verbose_name='File')),
                ('answer_num', models.CharField(blank=True, default='', max_length=1000)),
                ('created_by', models.CharField(blank=True, default='', max_length=1000, verbose_name='Create by')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ques_paper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.TestAdmin')),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
    ]
