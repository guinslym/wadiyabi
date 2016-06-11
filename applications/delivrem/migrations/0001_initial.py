# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import basis.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('updated_at', models.DateTimeField(default=basis.models._now, editable=False)),
                ('photo', models.ImageField(upload_to='delivrem/%Y/%m/%d', help_text='Show us wadiyabi')),
                ('slug', models.CharField(null=True, blank=True, max_length=220)),
                ('showoff', models.CharField(null=True, blank=True, max_length=440)),
                ('price', models.DecimalField(decimal_places=2, max_digits=16, null=True, blank=True)),
                ('activated', models.BooleanField(default=False)),
                ('sale', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
