# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='amount',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='item',
            name='picture',
            field=models.ImageField(upload_to='', null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
