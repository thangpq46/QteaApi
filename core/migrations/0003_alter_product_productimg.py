# Generated by Django 4.0.5 on 2022-07-04 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_product_productimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productimg',
            field=models.ImageField(db_column='IMG', max_length=255, upload_to='products/'),
        ),
    ]
