# Generated by Django 3.2.7 on 2021-09-20 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_mainimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mainimage',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
    ]