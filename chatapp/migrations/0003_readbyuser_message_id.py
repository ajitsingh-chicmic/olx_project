# Generated by Django 5.1.6 on 2025-04-01 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_readbyuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='readbyuser',
            name='message_id',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='chatapp.messageinfo'),
            preserve_default=False,
        ),
    ]
