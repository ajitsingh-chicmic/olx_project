# Generated by Django 5.1.6 on 2025-03-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_alter_products_subcategory_userfavourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='display_photo',
            field=models.ImageField(default=None, upload_to='Product_images/'),
        ),
    ]
