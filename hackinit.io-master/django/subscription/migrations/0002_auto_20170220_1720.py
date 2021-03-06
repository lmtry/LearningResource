# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionCellphoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cellphone_number', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionEmailAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_address', models.EmailField(unique=True, max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='SubscriptionEmail',
        ),
        migrations.DeleteModel(
            name='SubscriptionPhone',
        ),
    ]
