# Generated by Django 5.0.4 on 2024-04-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
