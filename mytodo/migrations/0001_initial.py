# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('done', models.CharField(default=b'N', max_length=1)),
                ('order', models.IntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
