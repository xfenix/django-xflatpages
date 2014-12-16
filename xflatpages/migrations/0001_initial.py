# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(help_text="\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: '/about/contact/'. \u0423\u0431\u0435\u0434\u0438\u0442\u0435\u0441\u044c, \u0447\u0442\u043e \u0432\u044b \u0434\u043e\u0431\u0430\u0432\u0438\u043b\u0438 \u0441\u043b\u0435\u0448 \u0432 \u043d\u0430\u0447\u0430\u043b\u043e \u0438 \u043a\u043e\u043d\u0435\u0446", max_length=255, verbose_name='URL', db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('cont', models.TextField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435', blank=True)),
                ('template_name', models.CharField(default=None, help_text='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0445 \u0448\u0430\u0431\u043b\u043e\u043d\u043e\u0432 (\u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044f /templates/flatpages/)', max_length=255, verbose_name='\u0428\u0430\u0431\u043b\u043e\u043d')),
            ],
            options={
                'ordering': ('url',),
                'verbose_name': '\u041f\u0440\u043e\u0441\u0442\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u041f\u0440\u043e\u0441\u0442\u044b\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
            bases=(models.Model,),
        ),
    ]
