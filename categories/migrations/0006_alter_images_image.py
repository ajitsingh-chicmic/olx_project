# Generated by Django 5.1.6 on 2025-04-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_alter_products_display_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
