# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('market', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('opening', models.CharField(max_length=200)),
                ('maximum', models.CharField(max_length=200)),
                ('minimum', models.CharField(max_length=200)),
                ('close', models.CharField(max_length=200)),
                ('volume', models.BigIntegerField()),
                ('amount', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
            ],
            options={
                'ordering': ('-time',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='quote',
            unique_together=set([('market', 'code', 'time')]),
        ),
    ]
