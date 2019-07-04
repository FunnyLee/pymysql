# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=True)),
                ('hcomment', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('hbook', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
