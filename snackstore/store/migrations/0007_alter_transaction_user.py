# Generated by Django 4.2.16 on 2024-11-28 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_created_at_product_stock_product_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.IntegerField(),
        ),
    ]