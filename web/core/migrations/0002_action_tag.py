# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('state', models.IntegerField(choices=[(0, 'to do'), (1, 'doing'), (2, 'review'), (3, 'done')], default=0)),
                ('task', models.ForeignKey(help_text='Designates task to be put in the action pipeline', on_delete=django.db.models.deletion.CASCADE, to='core.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, default='')),
                ('tasks', models.ManyToManyField(blank=True, to='core.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
